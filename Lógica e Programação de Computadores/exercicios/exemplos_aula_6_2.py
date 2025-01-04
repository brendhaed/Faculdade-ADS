
# Exemplo 1: implemente um programa que calcula a soma do n primeiros termos da serie:
# 1 + 1/2 + 1/3 + 1/4 + 1/5 +.....

nTermos = int(input("Digite o numero de termos: "))
if nTermos <= 0: print("Numero de termos invalido")
else:
 soma = 0
 cont = 1
while cont <= nTermos:
 soma = soma + 1/cont
 cont = cont + 1
print("Soma:", soma)

# Exemplo 2: implemente um programa que calcula a soma do n primeiros termos da serie:
# 2 + 4/2 + 6/5 + 8/7 + 10/9 +.....

nTermos = int(input("Digite o numero de termos: "))
if nTermos <= 0: print("Numero de termos invalido")
else:
 soma = 0
 cont = 1
 numerador = 2
 denominador = 1
while cont <= nTermos:
 soma = soma + numerador/denominador
 cont = cont + 1
 numerador = numerador + 2
 denominador = denominador + 2
print("Soma:", soma)

#Exemplo 3: implemente um programa que leia dois valores a e b.O programa deve escrevere somar os
#valores impares existentes entre a e b
a = int(input("Informe o valor inicial: "))
while a <= 0:
   print("Valor inicial invalido")
   a = int(input("Informe novamente o valor inicial: "))

b = int(input("Informe o valor final: "))
while b <= 0:
  print("Valor final invalido")
  b = int(input("Informe novamente o valor final: "))

# The following code block was incorrectly indented
if a > b:
    aux = a
    a = b
    b = aux

if a%2==0:
    a = a+1
soma = 0
print("Valores impares do intervalo:")
while a <= b:
    print(a)
    soma = soma + a
    a = a + 2
print("Soma dos impares do intervalo:", soma)

#Exemplo 4: Implemente um programa que leia um valor e verifique se é perfeito.
#Para ser perfeito, ele deve corresponde ‘a soma dos seus divisores próprios.
num = int(input("Digite um numero inteiro e positivo: "))
while num <= 0:
  print("Numero invalido, o numero deve ser positivo")
  num = int(input("Digite um numero inteiro e positivo: "))
soma = 0
d = 1
while d<=num/2:
 if num%d == 0: soma = soma + d
 d = d + 1
if soma == num: print("Número perfeito")
else: print("O numero não é perfeito")