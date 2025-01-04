
#Determinar as condições climáticas a partir de medições da temperatura e umidade atuais:
# Temperatura acima de 30, e clima úmido (mais de 60%)
# Temperatura acima de 30, e não úmido (menos de 60%)
# Temperatura de 20 a 30
# Temperatura de 10 a 20 (não incluindo)
# Temperatura inferior a 10

temperatura = float(input("Informe a temperatura:"))
umidade = int(input("Informe a umidade:"))
if temperatura >=30 and umidade>60:
  print("Clima úmido")
elif temperatura >=30 and umidade<60:
  print("Clima não úmido")
elif temperatura >=20 and temperatura <=30:
  print("Clima moderado")
elif temperatura >=10 and temperatura <20:
  print("Clima frio")
else:
  print("Clima muito frio")