import os

os.system('clear')

# Dictionaries

'''
 dictionaries são estrutudas de dados em python que armazem valores em pares chave-valor

 semelhante ao objetos em javascript 
'''

pessoa1 = {
  "nome": "Bruno",
  "idade": 23,
}

pessoa2 = {
  "nome": "Maria",
  "idade": 22,
}

pessoa3 = {
  "nome": "João",
  "idade": 21,
}

print("pessoa1")
print(f"length: {len(pessoa1)}")
print(f"Nome: {pessoa1['nome']}")
#print(pessoa1)

pessoa1['altura'] = 1.78 #adiciona uma nova chave-valor

# Duas formas de remover uma chave-valor
#pessoa1.pop('altura') 
del pessoa1['altura']

print(pessoa1["idade"])


grupo = {
  "p1": pessoa1, 
  "p2": pessoa2, 
  "p3": pessoa3
}

print(grupo)


"""
  lista de métodos:
  https://www.w3schools.com/python/python_ref_dictionary.asp
  
  - clear() limpa o dicionário 
  - copy() copia o dicionário
  - fromkeys() cria um dicionário com as chaves especificadas
  - get() retorna o valor associado a uma chave especificada
  - items() retorna uma lista de tuplas contendo as chaves e valores do dicionário
  - keys() retorna uma lista de chaves do dicionário
  - pop() remove o elemento com a chave especificada
  - popitem() remove o último elemento
  - setdefault() retorna o valor associado a uma chave especificada ou um valor 
  especificado se a
  - update() atualiza o dicionário com os pares chave-valor especificados
  - values() retorna uma lista de valores do dicionário
  - len() retorna o número de elementos do dicionário
  ...

"""