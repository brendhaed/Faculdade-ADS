#Exemplo 7: Algoritmo de Heronn para calcular a aproximação de raiz quadrada
num = int(input("Valor desejado: "))
total = int(input("Qtd. de repetições: "))
aprox = 1
anterior = 0
for cont in range(1, total + 1):
    aprox = (aprox + num/aprox) / 2
    print(f"{cont:3} {aprox:.5f}")
    dif = abs(aprox - anterior)
    if dif < 0.001:
        break
    anterior = aprox
print(f"Raiz aproximada: {aprox:.5f}")

#Exemplo 8:
soma = 0
for cont in range(10):
 alt = float(input("Digite uma altura:"))
 soma = soma + alt
 media = soma / 10
print(f"Média: {media:.3f}")

#Exemplo 9:
import random

soma = 0
maior = 0

for cont in range(10):
    alt = random.uniform(1.5, 2.10)
    soma = soma + alt
    if alt > maior:
        maior = alt

media = soma/10
print(f"Media: {media:.3f}")
print(f"Maior altura: {maior:.2f}")

#Exemplo 10:
import random

somaIdades = 0
cursoMaisVelho = ""
idadeMaisVelho = 0
qtdAlunos5oSem = 0

for cont in range(50):
    # Sorteio
    idade = random.randint(18, 60)
    curso = random.choice(["Eng. Civil", "Eng.Mec", "Eng. Química", "Eng. Prod."])
    semestre = random.randint(1, 10)

    # Coleta de estatísticas
    # Media de idades: é necessário somar as idades
    somaIdades += idade

    # Curso do aluno mais velho
    if idade > idadeMaisVelho:
        idadeMaisVelho = idade
        cursoMaisVelho = curso

    # Total de alunos no 5o. semestre
    if semestre == 5:
        qtdAlunos5oSem += 1

mediaIdades = somaIdades // 50

print(f"Media de idades: {mediaIdades}")
print(f"Curso do aluno mais velho ({idadeMaisVelho} anos): {cursoMaisVelho}")
print(f"Total de alunos no 5o. sem: {qtdAlunos5oSem}")