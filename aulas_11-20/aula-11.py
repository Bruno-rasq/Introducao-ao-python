import os 

os.system('clear') #limpando o terminal sempre antes de excutar um novo script


# TUPLAS: tuplas não podem ter ser valores diretamente modficados apos sua declaração

my_list = ["a", "b", "c", "d"]
my_tuple = (1, 2, 3, 4, 5)

my_list[0] = "z"
'''
  tuplas não suportam alterações, adicionar, remover e etc..
  porem podemos fazer uma conversão de uma tupla para uma lista e depois alterar ela

  Tuple = (1, 2, 3, 4, 5)
  List = list(Tuple)

  agora sim é possivel alterar os valores da lista

  List.append(8)

  Tuple = tuple(List)

  gambiarra.
''' 

print("minha tupla")
for x in my_tuple:
  print(x)

print("minha lista")
for y in my_list:
  print(y)

  
#length = len(my_tuple)
#help(length) o metodo help devolve a documentação de uma função
#print(length) exibi no console o tamanho da tupla

#print(my_tuple)