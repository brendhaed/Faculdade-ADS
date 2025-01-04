
print("Informe o horário de inicio")
hora_inicio = int(input("Hora:"))
minuto_inicio = int(input("Minutos:"))

print("Informe o horário do termino")
hora_termino = int(input("Hora:"))
minuto_termino = int(input("Minutos:"))

horario_inicial = hora_inicio * 60 + minuto_inicio
horario_final = hora_termino * 60 + minuto_termino

if horario_inicial < horario_final: duracao = horario_final - horario_inicial
else: duracao = 24*60 - horario_inicial + horario_final

print("Horas:", duracao //60)
print("Minutos:", duracao%60)

print("Informe um valor inteiro de 4 digitos:")
numero = int(input())

if numero <1111 or numero >9999: print("Valor fora do intervalo!")

milhar = numero//1000
resto = numero%1000
centena = resto//100
resto = resto%100
dezena = resto//10
unidade = resto%10

invertido = unidade*1000 + dezena*100 + centena*10 + milhar
print("Valor ao contrario:", invertido)
if numero == invertido: print("O numero é capicua")
else: print("O numero não é capicua")