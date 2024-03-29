import os

os.system('clear')

# MATRIX: matriz é um array com mais de uma dimensão

carros = ["bmw", "mercedes", "ford", "fiat"] #Array - list
carros2 = [
  ["a", "b"], 
  ["c", "d"], 
  ["e", 12]
] # matriz

# carros2[0].append("1")

#print(carros2[0][2])

# for x in carros2:
#   for y in x:
#     print(y)

for linha, coluna in carros2:
  print(linha, coluna, sep=" ", end="\n")