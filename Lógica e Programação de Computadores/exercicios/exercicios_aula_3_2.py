
valor = int(input("Informe um valor:"))
if valor >0: print("O valor digitado é positivo")

val = int(input("Informe um valor: "))
if val >0: print("Valor é positivo")
if val <0: print("Valor é negativo")
if val ==0: print("Valor é zero")

print("Informe um primeiro valor:")
v1 = int(input())
print("Informe um segundo valor:")
v2 = int(input())
print("Informe um terceiro valor: ")
v3 = int(input())

if v1>=v2 and v1>v3 : maior = v1
if v2>v1 and v2>=v3 : maior = v2
if v3>=v1 and v3>=v2 : maior = v3

print ("Maior: ",maior)

print("Informe um primeiro valor: ")
v1 = int(input())
print("Informe um segundo valor: ")
v2 = int(input())
print("Informe um terceiro valor: ")
v3 = int(input())
print ("Informe um quarto valor: ")
v4 = int(input())

maior = v1
if v2>maior : maior = v2
if v3>maior : maior = v3
if v4>maior : maior = v4

print("Maior: ", maior)

print("Informe o primeiro valor:")
v1 = int(input())
print("Informe o segundo valor:")
v2 = int(input())

if v1>v2:
  aux = v1
  v1 = v2
  v2 = aux

  print(v1, v2)