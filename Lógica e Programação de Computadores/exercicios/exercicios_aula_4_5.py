
#Exercício 1: determinar se o ano é bissexto ou não
ano = int(input("Digite o ano:"))
if (ano % 4 == 0 and ano % 100 !=0) or (ano % 400 == 0):
  print("O ano é bissexto")
else:
  print("O ano não é bissexto")

#Exercício 2:determinar o total de dias em um mês
mes = int(input("Digite o mês:"))
ano = int(input("Digite o ano:"))
if mes == 2:
  if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    dias = 29  # Indentação corrigida aqui
  else:
    dias = 28
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
  dias = 30
else:
  dias = 31
print(f"Total de dias {dias}")

#Exercício 3: cálculo do salario liquido
sal_bruto = float(input("Digite o salário bruto:"))
dep = int(input("Total dependentes: "))

if sal_bruto < 1212.01:
  alinss = 0.075
  parcinss = 0
elif sal_bruto <= 2427.35:
  alinss = 0.09
  parcinss = 18.18
elif sal_bruto <= 3641.03:
  alinss = 0.12
  parcinss = 91
else:
  alinss = 0.14
  parcinss = 163.82

inss = sal_bruto * alinss - parcinss

if inss > 828.39:
  inss  = 828.39

print("INSS",inss)

base = sal_bruto - inss - 189.59 * dep
print("Base para cálculo IRRF:", base)

#a aliquota do imposto e a parcela a deduzir
if base <=1903.98:
  aliqirrf = 0
  parcirrf =0
elif base <= 2826.65:
  aliqirrf = 0.075
  parcirrf = 142.8
elif base <= 3751.05:
    aliqirrf = 0.15
    parcirrf = 354.8
elif base <=4664.68:
    aliqirrf = 0.225
    parcirrf = 636.13
else:
    aliqirrf = 0.275
    parcirrf = 869.36

#parcela a deduzir
irrf = base * aliqirrf - parcirrf

liquido = sal_bruto - inss - irrf
print("Sálario liquido:", liquido)