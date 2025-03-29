#Exemplo 1: Abrangência de listas
lista = [1, 2, 3, 4, 5]
quadrados = [item ** 2 for item in lista] #eleva ao quadrado a lista
print(quadrados)
quadrados2 = [item ** 2 for item in lista if item % 2 == 0] #eleva somente os pares
print(quadrados2)

#Exemplo 2:escrevendo a matriz
matriz = [[1, 2, 4], [2, 3, 5], [3, 4, 5]]
for linha in matriz:
  print(linha)
  for coluna in linha:
        print(coluna)

#Exemplo 3: somando elementos
matriz = [[1, 2, 4], [2, 3, 5], [3, 4, 5]]
soma = 0
for linha in matriz:
    for elem in linha:
      soma = soma + elem
print("Soma dos elementos da matriz:", soma)

#Exemplo 4: somando uma linha
matriz = [[1, 2, 4], [2, 3, 5], [3, 4, 5]]
soma = 0
for elem in range(0,3):
  print(matriz[0][elem])
  soma = soma + matriz[0][elem]
print("Soma da linha 0: ", soma)

#Exemplo 5: somando uma coluna
matriz = [[1, 2, 4], [2, 3, 5], [3, 4, 5]]
soma = 0
for elem in range(0,3):
  print(matriz[elem][2])
  soma = soma + matriz[elem][2]
print("Soma da coluna 2: ", soma)

#Exemplo 6: somando a diagonal principal
matriz = [[1, 2, 4], [2, 3, 5], [3, 4, 5]]
soma = 0
for elem in range(0,3):
  print(matriz[elem][elem])
  soma = soma + matriz[elem][elem]
print("Soma da diagonal principal: ", soma)

#Exemplo 7: somando a diagonal secundária
matriz = [[1, 2, 4], [2, 3, 5], [3, 4, 5]]
soma = 0
coluna = 2
for linha in range(0,3):
  print(matriz[linha][coluna])
  soma = soma + matriz[linha][coluna]
  coluna = coluna - 1
print("Soma da diagonal secundária: ", soma)

#Exemplo 8: trocando linhas
matriz = [[1, 2, 4], [2, 3, 5], [3, 4, 5]]
print("Matriz original: ")
for linha in matriz:
  print(linha)

aux = matriz[0]
matriz[0] = matriz[2]
matriz[2] = aux
print("Matriz após a troca da linha 0 com a linha 2 ")
for linha in matriz:
  print(linha)

#Exemplo 9:trocando colunas
matriz = [[1, 2, 4], [2, 3, 5], [3, 4, 5]]
print("Matriz original: ")
for linha in matriz:
  print(linha)
for e in range(0,3):
  aux = matriz[e][0]
  matriz[e][0] = matriz[e][1]
  matriz[e][1] = aux
print("Matriz após a troca da coluna 0 com a coluna 1 ")
for linha in matriz:
  print(linha)

#Exemplo 10: totalizando cada linha
matriz = [[1, 2, 4], [2, 3, 5], [3, 4, 5]]
print("Matriz original: ")
somaLinha = []
for linha in matriz:
  print(linha)
  soma = 0
  for elem in linha:
    soma = soma + elem
  somaLinha.append(soma)
print("Total por linha ", somaLinha)

#Exemplo 11: totalizando cada coluna
matriz = [[1, 2, 4], [2, 3, 5], [3, 4, 5]]
print("Matriz original: ")
for linha in matriz:
  print(linha)
somaColuna = []
for col in range(0,3):
  soma = 0
  for linha in range(0,3):
    soma = soma + matriz[linha][col]
  somaColuna.append(soma)
  print("Total por coluna: ", somaColuna)

#Exemplo 12: gerando uma matriz randômica
import random
#Matriz 3x3
matriz = []
for linha in range(0,3):
  linha = []
  for coluna in range(0,3):
    linha.append(random.randint(0,10))
  matriz.append(linha)
print(matriz)

#Exercicio:
frases = ["eu estudo ads na pucrs",
          "um banco de dados é uma coleção organizada de informações",
          "SQL é uma linguagem de programação usada em bancos de dados relacionais"]
for sentenca in frases:
  print(sentenca)

#Tokenização
tokens = []
for sentenca in frases:
  tokens.append(sentenca.split())

for sentenca in tokens:
  print("Palavras da sentença: ", sentenca)
  for palavra in sentenca:
    print(palavra)
