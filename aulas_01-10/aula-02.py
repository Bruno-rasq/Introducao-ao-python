# Aula - 02 - Variaveis globais

curso = "voce ja fez o curso?"

def curso_python():
  print(curso)

curso_python()

def cs():
  c = "voce ainda nao fez o curso?"
  print(c)

cs()

# print(c) não é possível printar uma variável que foi criada dentro de uma função, 
#pois ela não é global.

def variavel_global():
  global global_var
  global_var = 'isso é uma variável global'

variavel_global()

print(global_var)