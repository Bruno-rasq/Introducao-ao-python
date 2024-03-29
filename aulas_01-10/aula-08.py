# list em python- ARRAYS

'''
metodos de list
  - append
  - remove
  - pop
  - insert
  - len
  - clear
  - list
'''

carros = ["ford", "ferrari", "mercedes", "bmw"]

'''
listas em python começam pelo indice 0 esquerda para direta 
ou direita para esquerda começando com -1

'''

print(carros[0]) #ford
print(carros[1]) #ferrari
print(carros[-1]) #bmw


# alterar um item da lista
carros[2] = "audi"

#em python utiliza-se o metodo appende para adicionar um item ao final da lista
carros.append("porsche") #equivalente ao push em javascript

#em python utiliza-se o metodo pop passando o indice do elemento que deseja excluir
carros.pop() #se não for passado o indice ele exclui o ultimo item

#ou pode se usar o metodo remove passando o elemento que deseja excluir
carros.remove("ferrari")


'''
tambem é possivel remover itens com a palavra reservada del seguida da list[indice]

del carros[0]
'''

del carros[0]



# metodo inserte passando o indice e o valor que deseja inserir
carros.insert(0, "fusca")

length = len(carros) ## retirna o tamanho da lista

cloneList = list(carros)