#Exemplo 1:contar ocorrências de um mesmo símbolo na lista
lista = ['a','b','a','b','c','d','a']
print(lista.count('a'))

#Exemplo 2: somar elementos de uma lista
lista = [1,10,9,15,5,2,8]
print(sum(lista))

#Exemplo 3: encontrar o menor e o maior valor da lista
lista = [1,10,9,15,5,2,8]
print(min(lista))
print(max(lista))

#Exemplo 4: ordenar uma lista
lista = [1,2,5,0,4,1,2,6,9,2]
lista2 = ['c','a','b','d','h','z']

lista.sort()
print("Ordem crescente",lista)
lista.reverse()
print("Ordem decrescente",lista)

lista2.sort()
print("Ordem crescente",lista2)
lista2.reverse()
print("Ordem decrescente",lista2)

#Exercicio exemplo:
import random

lista = []
for i in range(1,16):
  lista.append(random.randint(1,100)/10)
print("Notas:",lista)
media = sum(lista)//len(lista)
print("Média:",media)
acima = 0
abaixo = 0
for nota in lista:
  if nota>media: acima = acima + 1
  if nota<media: abaixo = abaixo + 1

print("Quantidades de notas acima da média:", acima)
print("Quantidades de notas abaixo da média:", abaixo)
print("Quabtidade de notas iguais a média:",lista.count(media))
print("Maior nota:" , max(lista))
print("Menor nota:", min(lista))