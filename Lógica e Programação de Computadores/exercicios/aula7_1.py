
# Exemplo 1
def exibe():
  """Exibe uma mensagem (docstring)"""
  print("Mensagem")
exibe()
exibe()
print("Outra mensagem")
exibe()

#Instalação do pacote ColabTurtlePlus:
#!pip3 install ColabTurtlePlus
from ColabTurtlePlus.Turtle import *

#Exemplo 2: Desenhando um quadrado
from ColabTurtlePlus.Turtle import *

clearscreen()
setup(600,400)
bob = Turtle()
bob.speed(6)
for lado in range(4):
  bob.forward(50)
  bob.right(90)

#Exemplo 3: desenhando vários quadrados
from ColabTurtlePlus.Turtle import *
clearscreen()
setup(600,400)
bob = Turtle()
bob.speed(6)
for lado in range(4):
  bob.forward(50)
  bob.right(90)

for quad in range(4):
 for lado in range(4):
  bob.forward(50)
  bob.right(90)
 bob.penup()
 bob.left(90)
 bob.forward(70)
 bob.right(90)
 bob.pendown()

#Exemplo 4: desenhando vários quadrados (código melhorado)
from ColabTurtlePlus.Turtle import *
clearscreen()
setup(600,400)
bob = Turtle()
bob.speed(6)
for lado in range(4):
  bob.forward(50)
  bob.right(90)

def quadrado():
 for lado in range(4):
  bob.forward(50)
  bob.right(90)

for quad in range(4):
 quadrado()
 bob.penup()
 bob.left(90)
 bob.forward(70)
 bob.right(90)
 bob.pendown()

#Exemplo 5:Adicionando um parâmetro à função quadrado: o comprimento do lado do quadrado
from ColabTurtlePlus.Turtle import *
clearscreen()
setup(600,400)
bob = Turtle()
bob.speed(6)
for lado in range(4):
  bob.forward(50)
  bob.right(90)

def quadrado(lado):
 for cont in range(4):
  bob.forward(lado)
  bob.right(90)

for quad in range(4):
 quadrado(30)
 bob.penup()
 bob.left(90)
 bob.forward(50)
 bob.right(90)
 bob.pendown()

#Exemplo 6: variando o tamanho do lado
from ColabTurtlePlus.Turtle import *
clearscreen()
setup(600,400)
bob = Turtle()
bob.speed(6)

for lado in range(4):
  bob.forward(50)
  bob.right(90)

def quadrado(lado):
 for cont in range(4):
  bob.forward(lado)
  bob.right(90)

tam = 20
for i in range(15):
 quadrado(tam)
 tam = tam + 10
 bob.forward(10)
 bob.right(18)