#Problema 1: Jogo da Velha

import random

# Gera o tabuleiro inicial do jogo
def geraTabuleiro():
  tabuleiro = []
  for col in range(0,3):
    linha = []
    for lin in range(0,3):
      linha.append('#')
    tabuleiro.append(linha)
  return tabuleiro

# Escreve o tabuleiro do jogo
def escreveTabuleiro(tabuleiro):
  print("\n-------------Jogo da Velha--------------")
  indices = [0,1,2]
  print("\t\t0\t1\t2")
  for i in indices:
    print("\t",i,"\t",end="")
    for j in indices:
      print(tabuleiro[i][j],"\t", end="")
    print()

# Jogada do computador
def jogaComputador(tabuleiro):
  linha = random.randint(0,2)
  coluna = random.randint(0,2)
  while tabuleiro[linha][coluna]!="#":
    linha = random.randint(0,2)
    coluna = random.randint(0,2)
  tabuleiro[linha][coluna]="O"

# Valida intervalo
def valida(valor):
  if valor>=0 and valor<=2:
    return True
  return False

# Jogada do usuario
def jogaUsuario(tabuleiro):
  print()
  linha = int(input("\tInforme a linha: "))
  coluna = int(input("\tInforme a coluna: "))
  while not(valida(linha)) or not(valida(coluna)) or not (tabuleiro[linha][coluna]=="#"):
    print("\tIndices fora do intervalo valido ou celula ocupada.")
    linha = int(input("\tInforme a linha: "))
    coluna = int(input("\tInforme a coluna: "))
  tabuleiro[linha][coluna] = "X"

# Verifica Linha
def verificaVencedorEmLinha(tabuleiro, caracter):
  for linha in tabuleiro:
    cont = 0
    for item in linha:
      if item==caracter: cont = cont + 1
      else:
        cont = 0
        break
    if cont==3: return True
  return False

# Verifica Coluna
def verificaVencedorEmColuna(tabuleiro, caracter):
  col = 0
  while col<=2:
    lin = 0
    cont = 0
    while lin <=2:
      if tabuleiro[lin][col]==caracter: cont = cont + 1
      else:
        cont = 0
        break
      lin = lin + 1
    if cont==3: return True
    col = col + 1
  return False

# Verifica diagonal
def verificaVencedorEmDiagonal(tabuleiro, caracter):
  cont = 0
  for i in range(0,3):
    if tabuleiro[i][i]==caracter: cont = cont+1
    else: break
  if cont==3: return True
  cont = 0
  for i in range(0,3):
    if tabuleiro[i][2-i]==caracter: cont = cont+1
    else: break
  if cont==3: return True
  return False

# Verifica vencedor
def verificaVencedor(tabuleiro, caracter):
  resultado = verificaVencedorEmLinha(tabuleiro,caracter)
  if resultado==True: return True
  resultado = verificaVencedorEmColuna(tabuleiro,caracter)
  if resultado==True: return True
  resultado = verificaVencedorEmDiagonal(tabuleiro,caracter)
  if resultado==True: return True
  return False

# Ciclo do jogo da velha
def jogoDaVelha():
  tab = geraTabuleiro()
  escreveTabuleiro(tab)
  jogaUsuario(tab)

  cont = 1
  vencedor = 0
  while cont<=4:
    jogaComputador(tab)
    r = verificaVencedor(tab,"O")
    if r==True:
      vencedor = 2
      break
    escreveTabuleiro(tab)
    jogaUsuario(tab)
    r= verificaVencedor(tab,"X")
    if r == True:
      vencedor=1
      break
    cont = cont + 1

  escreveTabuleiro(tab)
  if vencedor==0: print("\tDeu veia")
  else:
    if vencedor==2 : print("\tO computador venceu.")
    else:
      print("\tO usuario venceu.")
  return vencedor

# Grava vencedores
def gravaVencedor(nomeVencedor,arquivo):
  arq = open(arquivo,"a")
  arq.write(nomeVencedor+"\n")
  arq.close()

# Busca vencedores
def leArquivoVencedores(arquivo):
  try:
    arq = open(arquivo,"r")
  except FileNotFoundError:
    return []
  vencedores = []
  for linha in arq:
    vencedores.append(linha[:-1])
  return vencedores

#Escreve os dados de uma lista
def escreveLista(lista):
  print("\nVencedores: ")
  if lista==[]: print("Não há vencedores ainda")
  for item in lista:
    print(item)

while True:
  print(" \n\n---- M E N U ---- ")
  print("1 - Jogar ")
  print("2 - Ver vencedores")
  print("0 - Sair")
  print("\nInforme a opcao: ")
  op = int(input())
  if op == 0:
    print("Fim do programa")
    break
  else:
    if op == 1:
      vencedor = jogoDaVelha()
      if vencedor==0: #empate
        gravaVencedor("empate", "resultados.txt")
      else:
        if vencedor==1: #usuario ganhou
          nome = input("\tInforme o seu nome: ")
          gravaVencedor(nome, "resultados.txt")
        else: #computador ganhou
          gravaVencedor("computador", "resultados.txt")
    else:
      if op==2:
        dados = leArquivoVencedores("resultados.txt")
        escreveLista(dados)
      else: print("Opcao invalida")