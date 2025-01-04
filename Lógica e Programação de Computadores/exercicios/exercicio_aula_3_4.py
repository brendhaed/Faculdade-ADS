
preco = float(input("Informe o preço de custo:"))
if preco<0 : print("Valor inválido!")
else:
  if preco<10: venda = preco * 1.7
  if preco>=10 and preco<30: venda = preco * 1.5
  if preco>=30 and preco<50: venda = preco * 1.4
  if preco>=50: venda = preco * 1.3

  print("Preço de venda é", venda)