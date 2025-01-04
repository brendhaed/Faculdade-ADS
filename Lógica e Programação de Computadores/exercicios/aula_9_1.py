
#exemplo 1: plotando dados
import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[2,4,9,16])
plt.show()

#exemplo 2: preencendo uma lista e plotando
import matplotlib.pyplot as plt
listax = []
listay = []
for x in range(10):
    listax.append(x)
    listay.append(x**2)
plt.plot(listax,listay)
plt.show()

#exemplo 3: mudando o estilo traçado
import matplotlib.pyplot as plt

listax = [x for x in range (10)]
listay = [x**2 for x in range (10)]
plt.plot(listax,listay,'ro') #circulos vermelhos
plt.show()

#exemplo 4: desenhando mais de uma curva
import matplotlib.pyplot as plt
listax = [x for x in range (10)]
listay = [x**2 for x in range (10)]
listay2 = [x**3 for x in range (10)]
plt.plot(listax,listay,'r-')
plt.plot(listax,listay2,'bo')
plt.show()

#exemplo 5: adicionando rótulos e titulos ao grafico
import matplotlib.pyplot as plt
listax = [x for x in range (10)]
listay = [x**2 for x in range (10)]
listay2 = [x**3 for x in range (10)]

plt.plot(listax,listay,'r-', label= "$x^2$")
plt.plot(listax,listay2, 'bo', label = "$x^3$")

plt.title("$x^2$ e $x^3$")
plt.legend()
plt.show()

#exemplo 6: desenhando um grafico em barras
import matplotlib.pyplot as plt
import random

random.seed(42)
anos = [a for a in range (1990,2010)]
valores = [random.randint(100,1500) for v in range(len(anos))]

plt.bar(anos,valores)
plt.xticks(range(1990,2010,2))
plt.show()

plt.bar(anos,valores)
plt.show()
#

#exemplo 7: desenhando um histograma
import matplotlib.pyplot as plt
import random

random.seed(42)

valores = [random.randint(0,11) for v in range(100)]
x = [v + 0.5 for v in range(0,11)]
plt.hist(valores, x)
plt.show()

#exemplo 8:plotando dados a partir de um arquivo
import matplotlib.pyplot as plt

def carregaDados(nomeArq):
  aux = []
  with open(nomeArq) as csv:
    csv.readline()
    for linha in csv:
      nova = [float(val) for val in linha.split(",")]
      aux.append(nova)
  return aux

dados = carregaDados("sample_data/california_housing_test.csv")
longitudes = [aux[0] for aux in dados]
latitudes = [aux[1] for aux in dados]

#plt.plot(longitudes,latitudes,'bo')
plt.scatter(longitudes, latitudes,s=1)
plt.show()

#exemplo 9:
import folium

map = folium.Map(location=[36.7783, -119.4179],
                 zoom_start=6, min_zoom=5)
for aux in dados:
  folium.CircleMarker(radius=1, location=[aux[1], aux[0]]).add_to(map)

map