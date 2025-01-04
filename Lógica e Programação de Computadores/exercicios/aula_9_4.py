
#exemplo 20: Contagem de frequência das letras em um texto
import string
# Cria dicionario vazio
freq = {}
# Le o texto e passa para minusculas
texto = input("Texto:").lower()

# Para cada letra no texto:
for letra in texto:
  #Se for um espaço, pula
  if letra == " ": continue
  if letra not in freq:
    freq[letra] = 0
    # Incrementa a frequencia da letra (valor)
  freq[letra] = freq[letra] + 1
# Para cada chave...
for chave in sorted(freq.keys()):
  # Mostra a letra e a sua frequencia
  print(chave," => ",freq[chave])

# Usa conjuntos para descobrir as letras
# usadas e não usadas no texto
todasLetras = set(string.ascii_lowercase)
usadas = set(freq.keys())
naoUsadas = todasLetras - usadas

print(f"Letras usadas: {sorted(usadas)}")
print(f"Letras não usadas: {sorted(naoUsadas)}")

import urllib.request
url = "https://www.gutenberg.org/cache/epub/55752/pg55752.txt"
response = urllib.request.urlopen(url)
texto = response.read().decode('utf-8')
with open('texto.txt', 'w') as f:
  f.write(texto)

#exemplo 21:Contagem de frequência das palavras em um arquivo
import string
import nltk

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')
print(stopwords[:10])

# Cria dicionario vazio
freq = {}

with open("texto.txt") as arq:
  inicio = False
  # Para cada linha no texto:
  for linha in arq:
    linha = linha[:-1]
    if linha == 'I':
      inicio = True
    if not inicio or linha == "":
      continue
    linha = linha.lower()
    # Remove a pontuação da linha
    for pont in string.punctuation:
      linha = linha.replace(pont, "")
    # Processa cada palavra na linha
    for pal in linha.split(" "):
      if len(pal) < 3 or pal in stopwords:
        continue
      if pal not in freq:
        freq[pal] = 0
      freq[pal] = freq[pal] + 1

cont = 1
# Imprime as 30 palavras mais frequentes
for chave, valor in sorted(freq.items(), key=lambda x: x[1], reverse=True):
  print(f"{cont:3} - [{chave}] => {valor}")
  cont += 1
  if cont > 30:
    break

#!curl https://raw.githubusercontent.com/mflash/logicaeprogramacao/main/aula09/Unidades_Basicas_Saude-UBS.csv -o UBS.csv

#exemplo 22: consulta de dados a partir do arquivo
import folium
from folium.plugins import MarkerCluster

map = folium.Map(location=[-30,-51], zoom_start = 6, min_zoom=5)
marker_cluster = MarkerCluster().add_to(map)
unidades = {}

with open("UBS.csv") as csv:
  print(csv.readline()) # mostra cabeçalho
  for linha in csv:
    aux = linha[:-1].split(';')
    lat = aux[6]
    lon = aux[7]
    uf = aux[1]
    if lat != '' and lon != '' and uf == "43": # filtra somente o RS
      nome = aux[3][1:-1]
      logr = aux[4][1:-1]
      bairro = aux[5][1:-1]
      lat = float(lat)
      lon = float(lon)
      unidades[nome] = [logr,bairro,lat,lon]
      folium.Marker(popup=nome,location=[lat,lon]).add_to(marker_cluster)

map

#exemplo 22 (cont.): consultando os dados
ubs = input("Nome da UBS: ").upper()
# Consulta direta por chave (dicionário)
if ubs in unidades:
  print(unidades[ubs])
else:
  print("Não encontrada")
# Consulta parcial por chave (sequencial)
for nome in unidades.keys():
  if ubs in nome:
    print("Parcial: ",nome,unidades[nome])