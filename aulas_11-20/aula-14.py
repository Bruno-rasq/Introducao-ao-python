import os

os.system("clear")

#Funções:

# funcao_sem_parametro()
def hello():
    print("Hello World!")

# funcao_com_parametro(a, b)
def soma(a, b):
    print(a + b)

# funcao_com_retorno(a, b)
def somar(a, b):
    return a + b

# funcao com parametro padrão
def somar_com_padrao(a=0, b=0):
  return a + b

# funcao com parametro opcional
def apresentar(nome, idade=None):
  if idade is not None:
    print(f"Olá, meu nome é {nome}, tenho {idade} anos.")
  else:
    print(f"Olá, meu nome é {nome}.")


# funcao com parametros arbitrários
def multiplicar(*args):
  response=0
  for arg in args:
    response *= arg
  return response

#ou

def somarValores(array):
  response=0
  for n in array:
    response += n
  return response

