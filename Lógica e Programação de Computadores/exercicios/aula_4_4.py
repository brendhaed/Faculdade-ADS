
#Exemplo 10: jogo pedra, papel, tesoura:

import random

jogador = input("Sua escolha [Pe]dra,[Pa]pel, [T]esoura? ")
comp = random.choice(["Pe","Pa","T"])
print(f"Computador escolheu: {comp}")

if jogador == comp:
  print(f"Empate!")
elif jogador == "Pe":
  if comp == "T":
    print("Pe quebra T! Você ganhou!")
  else:
    print("Pa cobre Pe! Você perdeu")
elif jogador == "Pa":
  if comp == "Pe":
    print("Pa cobre Pe! Você ganhou!")
  else:
    print("T corta Pa! Você perdeu")
elif comp == "Pa":
  print("T corta Pa! Você ganhou!")
else:
  print("Pe quebra T! Você perdeu")

#Exemplo 11: determinação da situação em função da pressão arterial

sist = int(input("Sistólica: "))
diast = int(input("Diastólica: "))

if diast >= 120 or sist >=180:
    print("Crise hipertensiva")
elif (diast >=90 and diast < 120) or (sist >=140 and sist <180):
    print("Hipertensão estágio 2")
elif (diast >=80 and diast < 90) or (sist >=130 and sist < 140):
    print("Hipertensão estágio 1")
elif diast < 80 and sist < 130 and sist >=120:
    print("Elevada")
elif diast < 80 and sist < 120:
    print("Normal")