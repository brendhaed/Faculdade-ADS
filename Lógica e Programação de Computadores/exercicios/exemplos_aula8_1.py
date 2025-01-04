#Exemplo 1
lista = [] #lista vazia
lista1 = [1,2,3]
lista2 = ["o","menino","jogou","a","bola"]
lista3 = [1,2,3,"abacaxi","morango"]

print(lista1[2])
print(lista2[1])
print(lista3[0])
print(lista3[4])

#Exemplo 1: como percorrer uma lista com FOR
lista3 = [1,2,3,"abacaxi","morango"]

for item in lista3:
  print(item)

#Exemplo 1: como percorrer uma lista com WHILE
lista3 = [1,2,3,"abacaxi","morango"]

print("Quantidade de elemntos:", len(lista3))
indice = 0
while indice < len(lista3):
  print(lista3[indice])
  indice = indice + 1

#Exemplo 2: concatenar listas
lista = []
lista1 = ["o","menino","jogou","a","bola"]

lista = lista + [1]
print(lista)
lista = lista + [2]
print(lista)
lista2 = lista + lista1
print(lista2)
lista3 = ['a','b','c'] + lista2
print(lista3)

#Exemplo 3: como repetir os elementos de uma lista
lista = []
lista1 = ["o","menino","jogou","a","bola"]
lista2 = [1,2,3]

lista3 = lista2 * 3
lista4 = lista1 * 2
lista5 = lista * 4
print(lista3)
print(lista4)
print(lista5)

#Exemplo 4: como verificar se um elemento está na lista
lista = []
lista1 = ["o","menino","jogou","a","bola"]
lista2 = [1,2,3]

if "menino" in lista1: print("achou")
if "menino" in lista: print("pertence a lista")
else:print("não pertence a lista")
valor = int(input("Informe um valor:"))
if valor in lista2: print("pertence a lista")
else:print(valor, "não pertence a", lista2)

#Exemplo 5: acrescentar elementos na lista com append(insere item no final da lista)
lista = []
lista1 = ["o","menino","jogou","a","bola"]

lista.append('linguagem')
lista.append('python')
lista.append(lista1)
print(lista)

#Exemplo 5: acrescentar elementos na lista (outra forma)
lista2 = []
lista2.append('linguagem')
lista2.append('python')
for item in lista1:
  lista2.append(item)
print(lista2)

#Exemplo 6: acrescentar elementos na lista com insert(insere em qualquer posição)
lista = []
lista1 = ["o","menino","jogou","a","bola"]

lista.insert(0,'linguagem')
lista.insert(0,'python')
lista.insert(1, lista1)
lista.insert(2, "logica")
print(lista)

#Exemplo 7: invertendo a lista
lista2 = []
for item in lista1:
  lista2.insert(0,item)
print(lista2)

#Exemplo 8: Excluir elementos da lista usando POP
lista = []
lista1 = ["o","menino","jogou","a","bola"]

lista1.pop()
print(lista1)
lista1.pop(1)
print(lista1)

#Exemplo 9: Excluir elementos da lista usando REMOVE
lista = []
lista1 = ["o","menino","jogou","a","bola"]

lista1.remove("a")
print(lista1)
lista2 = ["a"] * 4
print(lista2)
lista2.remove("a")
print(lista2)

#Exercicio
import random

lista = []
for i in range(1,31):
  lista.append(random.randint(1,501))
print(lista)

maior  = lista [0]
pares = 0
for num in lista:
  if num > maior: maior = num
  if num % 2 == 0: pares = pares + 1
print("Maior:", maior)
print("Qtd de pares:", pares)