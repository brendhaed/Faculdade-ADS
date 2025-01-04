
valor = int(input("Informe valor inteiro de 1 a 7:"))
if valor<1 or valor>7:
    print("Valor fora do intevalo")
else:
    if valor==1: print("Domingo")
    if valor==2: print("Segunda")
    if valor==3: print("Terça")
    if valor==4: print("Quarta")
    if valor==5: print("Quinta")
    if valor==6: print("Sexta")
    if valor==7: print("Sábado")

nota1 = float(input("informe a nota 1:"))
nota2 =  float(input("informe a nota 2:"))
nota3 =  float(input("informe a nota 3:"))
if nota1<0 or nota1>10 or nota2<0 or nota2>10 or nota3<0 or nota3>10:
  print("Notas fora do intervalo!")
else:
  maior = nota1
  if nota2>maior:maior = nota2
  if nota3>maior:maior = nota3
media = 0.5*maior+0.25*(nota1+nota2+nota3-maior)
print("Média ponderada:", media)

import math
a = float(input("Informe o coeficiente a:"))
b = float(input("Informe o coeficiente b:"))
c = float(input("Informe o coeficiente c:"))

delta = math.pow(b,2) - 4*a*c
if delta <0 or a==0: print("Erro, delta negativo ou divisão por 0")
else:
  x1 = (-b + math.sqrt(delta))/(2*a)
  x2 = (-b - math.sqrt(delta))/(2*a)

print("x1 é:",x1)
print("x2 é:",x2)

saldo = float(input("Informe o saldo médio da conta:"))
if saldo<500:print("Não há limite")
if saldo>=500 and saldo<1000: print("Limite:",saldo*0.08)
if saldo>1000: print("Limite:", saldo*0.15)