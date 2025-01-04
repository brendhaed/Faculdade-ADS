
#Exercicio 1: Foram vendidas 50 peças de roupa. De cada peça foram coletados os seguintes dados: tamanho (P,M ou G) e cor
#(branco, preto ou azul). O programa deve ler os dados das peças de roupas e organizá-los em uma lista de tuplas, onde cada tupla
#é da forma (tamanho, cor). O programa deve ainda calcular e escrever: o tamanho que mais vendeu, a quantidade de peças de
#tamanho M que foram vendidas e a cor preferida pelos clientes.

peças = []
for i in range(1,6):
  print("Cont", i)
  tamanho = input("Informe o tamanho usando os valores P, M ou G:")
  while(tamanho != "P" and tamanho != "p" and tamanho != "M" and tamanho != "m" and tamanho != "G" and tamanho != "g"):
    tamanho = input("Informe o tamanho usando os valores P, M ou G:")
  op = int(input("Informe a cor usando 1 para Branco, 2 para preto, 3 para azul: "))
  while(op < 1 or op >3):
    op = int(input("Informe a cor usando 1 para Branco, 2 para Preto, 3 para azul: "))
  if op == 1: tupla = (tamanho,"branco")
  else:
    if op == 2: tupla = (tamanho,"preto")
    else: tupla = (tamanho,"azul")
  peças.append(tupla)
print("\n")
print(peças)

contP = 0
contM = 0
contG = 0
cores = []
for item in peças :
  if item[0] == "P" or item[0] == "p": contP += 1
  else:
    if item[0] == "M" or item[0] == "m": contM += 1
    else: contG = contG + 1
  cores.append(item[1])


totalizaTamanho = []
totalizaTamanho.append(("Pequeno",contP))
totalizaTamanho.append(("Medio",contM))
totalizaTamanho.append(("Grande",contG))
print(totalizaTamanho)
print("\n")

#Qual tamanho mais vendeu
maior = 0
tamanho = ""
for item in totalizaTamanho:
  if item[1] > maior:
    maior = item[1]
    tamanho = item[0]
print("Tamanho que mais vendeu:",tamanho, "vendeu", maior,"peças")
print("\n")

#Qtd de peças de tamanho M que foram vendidas
print("Quantidade de tamanho M vendido:", totalizaTamanho[1][1])
print("\n")

#Cor que mais vendeu
print("Quantidade de cores branco:", cores.count("branco"))
print("Quantidade de cores preto:", cores.count("preto"))
print("Quantidade de cores azul:", cores.count("azul"))

maior_cor_qtd = 0
cor_mais_vendida = ""
for cor in ["branco", "preto", "azul"]:
    qtd_cor = cores.count(cor)
    if qtd_cor > maior_cor_qtd:
        maior_cor_qtd = qtd_cor
        cor_mais_vendida = cor
        print("\n")
        print("Cor que mais vendeu:", cor_mais_vendida, "vendeu", maior_cor_qtd, "peças")