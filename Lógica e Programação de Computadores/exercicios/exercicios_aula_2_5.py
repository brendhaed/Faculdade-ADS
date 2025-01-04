
print("Informe o valor em fahrenheit:")
f = float(input())
c = 5/9 *(f-32)
print ("Celsius:", c)

import math

print("Informe um valor:")
valor1 = int(input())
print("Informe um segundo valor: ")
valor2 = int(input())

soma = valor1 + valor2
print("Soma:",soma)

diferenca = valor1 - valor2
print("Diferença:", diferenca)

media = (valor1 + valor2) /2
print("Média entre os valores é: ",media)

distancia = math.fabs(valor1-valor2)
print("Diferença exata:",distancia)

maior = (valor1+valor2+math.fabs(valor1-valor2))/2
print("O maior valor é ", maior)

menor = (valor1+valor2-math.fabs(valor1-valor2))/2
print("O menor valor é: ",menor)

print("Informe o tempo em segundos:")
tempo=int(input())

horas = tempo//3600
print("Horas:",horas)
resto = tempo%3600
minutos = resto//60
print("Minutos:", minutos)
segundos= resto % 60
print("Segundos:", segundos)

print(" Digite um valor inteiro de 4 digitos:")
valor = int(input())
milhar = valor//1000
resto = valor%1000
centena = resto//100
resto = resto%100
dezena = resto//10
unidade = resto%10

print("Valor invertido:", unidade*1000 + dezena*100 + centena*10 + milhar)