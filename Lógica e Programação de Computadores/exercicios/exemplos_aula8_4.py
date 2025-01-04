#Exemplo 1: Abrir arquivo para ler
arq = open("planta_iris.data", "r")
for linha in arq:
  valores = linha.split(",")
  print(valores)
arq.close() #deve fechar o arquivo depois de abrir

#Exemplo 2: Abrir para gravar
ref_arquivo = open("dados.txt","w")
cont = 1
while cont <= 3:
  nome = input("Digite seu nome: ")
  ref_arquivo.write(nome + "\n")
  cont = cont + 1
ref_arquivo.close()

#Exemplo 3: Abrir para gravar ao final
ref_arquivo = open("dados.txt","a")
cont = 1
while cont <= 3:
  nome = input("Digite seu nome: ")
  ref_arquivo.write(nome + "\n")
  cont = cont + 1
ref_arquivo.close()

#Exemplo 4:
arq = open("planta_iris.data", "r")
dados = []
for linha in arq:
  valores = linha.split(",")
  print(valores)
  ultima = valores[4][:-1]
  tupla = (float(valores[0]),float(valores[1]), float(valores[2]), float(valores[3], ultima))
  print(tupla)
  dados.append(tupla)
arq.close()
print(dados)

#Exemplo de exercicio:
arquivo = open("alturas.txt","w")
cont = 1
while cont <= 5:
  nome = input("Digite seu nome: ")
  altura = float(input("Digite sua altura: "))
  arquivo.write(nome + "-" + str(altura) + "\n")
  cont = cont + 1
arquivo.close()

lista = []
soma = 0
alturaAlto = -1
nomeAlto = ""
arquivo = open("alturas.txt","r")
for linha in arquivo:
  saida = linha[: -1].split('-')
  altura = float(saida[1])
  nome = saida[0]
  dados = (nome, altura)
  soma = soma + altura

  if altura > alturaAlto:
    alturaAlto = altura
    nomeAlto = nome
  lista.append(dados)
arquivo.close()
print(lista)
print("Média:", soma/len(lista))
print("Nome do mais alto:", nomeAlto)