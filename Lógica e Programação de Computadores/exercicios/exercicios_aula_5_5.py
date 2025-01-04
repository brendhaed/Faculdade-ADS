
#Exercício 1:Jogo da adivinhação
# 10 tentativas para adivinhar um número sorteado entre 1 a 100
# Computador informa se o número é maior ou menor que o digitado

import random

sorteado = random.randint(1,100)
#print(f"Sorteado: {sorteado}")
tentativas = False
for tent in range(1,11):
  print(f"Tentativa {tent}:", end="")
  num = int(input())
  if num < sorteado:
    print("Tente um número maior")
  elif num > sorteado:
    print("Tente um número menor")
  else:
    tentativas = True
    break

if tentativas:
    print("Você acertou!")
else: print(f"Você perdeu o número era:{sorteado}")

#Exercicio 2:
import random

somaRendas = 0
somaIdades = 0
qtdMais3Filhos = 0
qtdHomensMenor30 = 0
somaFilhos = 0
rendaHomemMaisVelho = 0
idadeHomemMaisVelho = 0
idadeMulherMaiorRenda = 0
mulherMaiorRenda = 0
totalHabitantes = 2000


for cont in range(2000):
 idade = random.randint(18,80)
renda = random.randint(1200,12000)
genero = random.choice(["m","f"])
qtdFilhos = random.randint(0,5)

#1. media de rendas
somaRendas += renda
#2. media de idade com mais de 3 filhos
if qtdFilhos > 3:
    somaIdades += idade
    qtdMais3Filhos += 1
#3. quantidade de homens com menos de 30 anos
if genero == "m" and idade < 30:
    qtdHomensMenor30 += 1
#4. media numero de filhos
somaFilhos += qtdFilhos
#5. renda homem mais velho
if genero == "m" and idade > idadeHomemMaisVelho:
   idadeHomemMaisVelho = idade
   rendaHomemMaisVelho = renda
#6. idade mulher com maior renda
if genero == "f" and renda > mulherMaiorRenda:
    idadeMulherMaiorRenda = idade
    mulherMaiorRenda = renda

# Resultados
mediaRenda = somaRendas / totalHabitantes
mediaMais3Filhos = somaIdades // qtdMais3Filhos if qtdMais3Filhos else 0
mediaFilhos = somaFilhos // totalHabitantes

print(f"Media de rendas: {mediaRenda}")
print(f"Media de idade com mais de 3 filhos: {mediaMais3Filhos}")
print(f"Quantidade de homens com menos de 30 anos: {qtdHomensMenor30}")
print(f"Media numero de filhos: {mediaFilhos}")
print(f"Renda homem mais velho: {rendaHomemMaisVelho}")
print(f"Idade mulher com maior renda: {idadeMulherMaiorRenda}")