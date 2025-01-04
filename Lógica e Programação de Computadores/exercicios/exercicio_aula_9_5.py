
#importar dados
#!curl https://raw.githubusercontent.com/mflash/logicaeprogramacao/main/aula09/partidos-fake.csv -o partidos-fake.csv
#!curl https://raw.githubusercontent.com/mflash/logicaeprogramacao/main/aula09/eleicoes-municipais-fake.csv -o eleicoes-municipais-fake.csv

#exercicio pt1: : determinar a composição da Câmara Municipal de uma determinada cidade
cid = input("Cidade:").upper()
vagas = int(input("Vagas:"))

partidos = {}   # nome, total de votos, vagas (quoc. part) e media
votos = {}      # sigla e total de votos
totalGeral = 0

with open("partidos-fake.csv") as csv:
  csv.readline()
  for linha in csv:
    dados = linha[:-1].split(",")
    aux = { 'nome': dados[1], 'votos': 0, 'vagas': 0,
           'media': 0}
    partidos[dados[0]] = aux

with open("eleicoes-municipais-fake.csv") as csv:
  csv.readline()
  for linha in csv:
    dados = linha[:-1].split(",")
    cidade = dados[1]
    sigla = dados[2]
    cargo = dados[3]
    nome = dados[4]
    totalVotos = int(dados[5])
    if cidade != cid or cargo != "VEREADOR":
      continue
    if nome not in votos:
      votos[nome] = { "sigla": sigla, "votos": 0}
    votos[nome]["votos"] += totalVotos
    partidos[sigla]["votos"] += totalVotos
    totalGeral += totalVotos


print(partidos)

#exercicio pt2:
print(f"Total votos: {totalGeral}")
qe = totalGeral//vagas
print(f"QE: {qe}")

# Calcula as vagas iniciais
somaVagas = 0

for sigla,dados in partidos.items():
  qp = dados['votos']//qe
  if qp > 0:
    dados['vagas'] = qp
    somaVagas += qp
    print(sigla,dados)

print()
print("Total de vagas já ocupadas:",somaVagas)
print()

#exercicio pt3:
# Calcula a média de cada partido, de acordo com o total de votos e as vagas já recebidas

for sigla,dados in partidos.items():
  me = dados['votos']//(dados['vagas']+1)
  dados['media'] = me
  #print(sigla,dados)

# Distribuir vagas disponíveis para cada partido, em ordem decrescente
# de media
for sigla,dados in sorted(partidos.items(), key=lambda x:x[1]['media'],
                          reverse=True):
  if somaVagas < vagas:
    dados['vagas'] += 1
    somaVagas += 1

#print(f"Total vagas ocup.: {somaVagas}")

salvaVagas = {} # armazena o total de vagas original para cada partido
for p in partidos:
  salvaVagas[p] = partidos[p]['vagas']

# Finalmente, passa por todos os candidatos, em ordem decrescente de votos,
# e enquanto houver vagas para o partido, mostra que foi eleito (e diminui uma
# vaga do partido)

for nome,dados in sorted(votos.items(), key=lambda x:x[1]['votos'], reverse=True):
  sigla = dados['sigla']
  if partidos[sigla]['vagas'] > 0:
    print(f"{nome:40} {sigla:4} {dados['votos']} votos")
    partidos[sigla]['vagas'] -= 1

#exercicio pt4
import matplotlib.pyplot as plt

print(salvaVagas)

totalFinalVagas = 0
nomes = []
valores = []

# Monta a lista de nomes (siglas) e valores (total de votos) para o gráfico
for p in salvaVagas:
  if salvaVagas[p] > 0:
    nomes.append(p)
    valores.append(salvaVagas[p])
    totalFinalVagas += salvaVagas[p]

print()
print("Total de vagas ocupadas:",totalFinalVagas)
print()

plt.figure(figsize=(10,4))
plt.xticks(rotation=30, ha='right')
plt.bar(nomes,valores)
plt.show()