#Resolução do projeto parte I: Dados meteorológicos do ano de 2021
somaTemperaturas = 0
temperaturaMediaMaximaAnual = 0
qtdDeMesesEscaldantes = 0
mesMaisEscaldanteDoAno = 0
mesMenosQuenteDoAno= 0

#Meses do ano e temperaturas:
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
"Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas =[]

#Instrução de entrada do usuário:
print("Digite a temperatura máxima dos meses do ano em graus Celsius: ")
print("\n")
for mes in range(1, 13):
    while True:
        temperatura = float(input(f"Digite a temperatura máxima do mês {mes}: "))
        if -60 <= temperatura <= 50:
            temperaturas.append(temperatura)
            break
        else:
            print("Temperatura inválida! Deve estar entre -60 e 50 graus Celsius. Digite novamente:")

print(temperaturas)
print("\n")
#1. Temperatura média anual:
somaTemperaturas = sum(temperaturas)
temperaturaMediaAnual = somaTemperaturas // 12
print(f"A temperatura média anual é de: {temperaturaMediaAnual} graus Celsius")

print("\n")
#2. Quantidade de meses escaldantes:
qtdDeMesesEscaldantes = sum(1 for temp in temperaturas if temp > 33)
print(f"Quantidade de meses escaldantes: {qtdDeMesesEscaldantes}")

print("\n")
#3. Mês mais escaldante do ano:
mesMaisEscaldanteDoAno = max(temperaturas)
mesMaisEscaldanteDoAno = meses[temperaturas.index(mesMaisEscaldanteDoAno)]
print(f"O mês mais escaldante do ano é: {mesMaisEscaldanteDoAno}")

print("\n")
#4. Mês menos quente do ano:
mesMenosQuenteDoAno = min(temperaturas)
mesMenosQuenteDoAno = meses[temperaturas.index(mesMenosQuenteDoAno)]
print(f"O mês menos quente do ano é: {mesMenosQuenteDoAno}")
