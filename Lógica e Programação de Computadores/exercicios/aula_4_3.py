#Exemplo 7: Variação do exemplo 5 (versão encadeada)
nota = int(input("Nota: "))

if nota >=90:
  print("Conceito A")
elif nota >=80:
  print("Conceito B")
elif nota >=70:
  print("Conceito C")
elif nota >=60:
  print("Conceito D")
else:
  print("Conceito F")

#Exemplo 8: total de dias em mes qualquer de 1-12 (sem bissextos)
mes = int(input("Mês: "))
if mes == 2:
  dias = 28
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
  dias = 30
else:
  dias = 31
print(f"Total de dias: {dias}")

#Exemplo 9: classificação a partir do cálculo do IMC:
altura = float(input("Altura (m):"))
peso = float(input("Peso (kg):"))
imc = peso/altura**2
print(f"Seu IMC é: {imc}")

if imc < 18.6:
  print("Abaixo do peso")
elif imc < 25:
  print("Peso normal")
elif imc < 30:
  print("Sobrepeso")
elif imc < 35:
  print("Obesidade grau 1")
elif imc < 40:
  print("Obesidade grau 2")
else:
  print("Obesidade grau 3 (severa)")