#Problema: Parte I - Faça um programa em Python que processe o arquivo disponibilizado com dados da planta Iris.
# Gere um novo arquivo com uma amostra do arquivo original. A amostra deve ter 30% dos dados originais.

import matplotlib.pyplot as plt
import random

#Leitura do arquivo
def cargaDados(nome):
  arquivo = open(nome,"r")
  dados = []
  for linha in arquivo:
    linha1 = linha[:-1]  #retira \n
    dados.append(linha1)
  arquivo.close()
  return dados

#Escreve os dados de uma lista
def escreveLista(lista):
  for item in lista:
    print(item)

#Excluindo o cabecalho
def geraListaSemCabecalho(lista):
  nova = []
  ind = 1
  while ind < len(lista):
    nova.append(lista[ind])
    ind = ind + 1
  return nova

#Misturando os dados
def misturando(lista, quantidade):
  while quantidade>0:
    quantidade = quantidade - 1
    ind1 = random.randint(0,len(lista)-1)
    ind2 = random.randint(0,len(lista)-1)
    aux = lista[ind1]
    lista[ind1] = lista[ind2]
    lista[ind2] = aux

#Criando uma amostra
def amostragem(lista, indice):
  misturando(lista,90)
  #escreveLista(lista)
  quantidade = len(lista)*indice
  amostra = []
  cont = 0
  while cont<quantidade:
    amostra.append(lista[cont])
    cont = cont + 1
  return amostra

#Grava amostra
def gravaAmostra(cabecalho,amostra, nome):
  arquivo = open(nome,"w")
  arquivo.write(cabecalho+"\n")
  for item in amostra:
    arquivo.write(item+"\n")
  arquivo.close()

plantas = cargaDados("planta_iris.data")

#escreveLista(plantas)
cabecalho = plantas[0]
#print(cabecalho)
plantas1 = geraListaSemCabecalho(plantas)

#escreveLista(plantas1)
amostra = amostragem(plantas1,0.3)
escreveLista(amostra)
gravaAmostra(cabecalho, amostra,"amostraIris.txt")

#Problema: Parte II - Usando a amostra, calcule e escreva:

# a) distribuicao em percentuais das amostras por classe (tipo de planta iris)
# b) a classe com maior numero de amostras
# c) exiba os dados por classe (tipo de planta iris) usando um grafico de barras
# d) para cada atributo (campo) numerico determine o valor minimo, o valor maximo e a media

import matplotlib.pyplot as plt
import random

# Leitura do arquivo
def cargaDados(nome):
  arquivo = open(nome,"r")
  dados = []
  for linha in arquivo:
    #print(linha)
    linha1 = linha[:-1]  #retira \n
    dados.append(linha1)
  arquivo.close()
  return dados

#Excluindo o cabecalho
def geraListaSemCabecalho(lista):
  nova = []
  ind = 1
  while ind < len(lista):
    nova.append(lista[ind])
    ind = ind + 1
  return nova

#Escreve os dados de uma lista
def escreveLista(lista):
  for item in lista:
    print(item)

# Conta amostras por classe
def contaAmostras(amostra, tiposPlantas):  #[0:"Iris-virginica",1:"Iris-setosa",2:"Iris-versicolor"]
  cont0 = 0
  cont1 = 0
  cont2 = 0
  for item in amostra:
    if tiposPlantas[0] in item: cont0 = cont0 + 1
    else:
      if tiposPlantas[1] in item: cont1 = cont1 + 1
      else: cont2 = cont2 + 1
  return [cont0, cont1, cont2]

# Gera grafico por tipo
def geraGrafico(tipos, quantidades):
  plt.bar(tipos,quantidades,color="blue")
  plt.title("Distribuicao das amostras por tipo de planta",color="blue")
  plt.xlabel("Tipos de Plantas",color="blue")
  plt.ylabel("Quantidade de Amostras",color="blue")
  plt.show()

# Dados dos atributos numericos
def analisaAtributosNumericos(cabecalho,dados):
  lista0 = []
  lista1 = []
  lista2 = []
  lista3 = []
  for item in dados:
    colunas = item.split(',')
    lista0.append(float(colunas[0]))
    lista1.append(float(colunas[1]))
    lista2.append(float(colunas[2]))
    lista3.append(float(colunas[3]))
  itens = cabecalho.split(",")
  print(itens[0], "\t - Minimo: ", min(lista0), " - Maximo: ", max(lista0), " Media: ", sum(lista0)/len(lista0))
  print(itens[1], "\t - Minimo: ", min(lista1), " - Maximo: ", max(lista1), " Media: ", sum(lista1)/len(lista1))
  print(itens[2], "\t - Minimo: ", min(lista2), " - Maximo: ", max(lista2), " Media: ", sum(lista2)/len(lista2))
  print(itens[3], "\t - Minimo: ", min(lista3), " - Maximo: ", max(lista3), " Media: ", sum(lista3)/len(lista3))

amostra = cargaDados("amostraIris.txt")
#escreveLista(amostra)
cabecalho = amostra[0]
#print(cabecalho)
amostra1 = geraListaSemCabecalho(amostra)
tipos = ["Iris-virginica","Iris-setosa","Iris-versicolor"]
quantidades = contaAmostras(amostra1,tipos)

ind = 0
classe = tipos[0]
maior = quantidades[0]
print("Resultados: \n")
while ind<len(tipos):
  print(tipos[ind]," - amostras: ", quantidades[ind], "(", (quantidades[ind]*100)/len(amostra1), "%)")
  if quantidades[ind]>maior:
    maior = quantidades[ind]
    classe = tipos[ind]
  ind = ind + 1
print("Total de amostras: ", len(amostra1))
print("\nTipo com mais amostras: ", classe,"\n")
geraGrafico(tipos,quantidades)
analisaAtributosNumericos(cabecalho,amostra1)