
#exemplo 14: operações basicas de um dicionário
dic = {}
dic["Fulano"] = "99817-9123"
dic["Beltrano"] = "99671-7562"
dic["Ciclano"] = "99881-1642"
nome = ""
while nome != "fim":
  nome = input("Nome a procurar (fim para encerrar): ")
  if nome != "fim":
    if nome in dic:
      print(f"Telefone: {dic[nome]}")
    else:
      print("Nome não encontrado!")

#exemplo 15: removendo chaves e valores
nome = ""
while nome != "fim":
  print(f"Tamanho do dicionário: {len(dic)}")
  print(dic)
  nome = input("Nome a remover (fim para encerrar): ")
  if nome != "fim":
    if nome in dic:
      del dic[nome]
      print("Nome removido!")
    else:
      print("Nome não encontrado!")

#exemplo 16: outras opções de acesso:
dic = {}

dic["Fulano"] = "99817-9123"
dic["Beltrano"] = "99671-7562"
dic["Ciclano"] = "99881-1642"

print(dic.keys())
print(dic.values())
print(dic.items())

print(f"Telefone de Fulano: {dic.get('Fulano')}")
print(f"Telefone de Veltrano: {dic.get('Veltrano')}")

#exemplo 17: explorando opções de acesso
dic = {}

dic["Fulano"] = "99817-9123"
dic["Beltrano"] = "99671-7562"
dic["Ciclano"] = "99881-1642"
dic["Pedro"] = "99123-2432"

for k in dic.keys():
  print(f"Chave: {k}")
for v in dic.values():
  print(f"Valor: {v}")
  print("Chaves e valores em ordem de inclusão:")
for k,v in dic.items():
  print(f"{k:8} -> {v}")
  print("Ordenado pelas chaves:")
for k,v in sorted(dic.items()):
  print(f"{k:8} -> {v}")
  print("Ordenado pelos valores:")
for k,v in sorted(dic.items(),key=lambda x: x[1]):
  print(f"{k:8} -> {v}")

#exemplo 18: explorando as operações sobre conjuntos(1)
a = set()
op = ""
while op != "fim":
  print(f"Conjunto: {a}")
  print()
  print("Digite um valor a inserir no conjunto:")
  op = input("pop para remover um elemento, fim para encerrar: ")
  if op == "pop":
    if len(a) < 0:
      print("Conjunto está vazio!")
    else:
      v = a.pop()
      print(f"Valor removido: {v}")
  else:
    a.add(op)

#exemplo 19: explorando as operações sobre conjuntos(2)
a = set([1,2,3,4,5,6])
b = set([4,5,6,7,8,9])
c = set([1,3,5])

print(f"união a+b: {a.union(b)}")
print(f"diferença a-b: {a.difference(b)}")
print(f"diferença b-a: {b.difference(a)}")
print(f"intersec. a&b: {a.intersection(b)}")
print(f"dif. sim. a^b: {a.symmetric_difference(b)}")

print(f"a contém c : {a.issuperset(c)}")
print(f"c contido a : {c.issubset(a)}")