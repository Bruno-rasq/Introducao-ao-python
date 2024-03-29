# loop em python

# for:

animais = ["gato", "cachorro", "papagaio", "coelho", "pato"]

for x in animais:
  print(x)
  if x == "coelho":
    print("é tarde! é tarde!")
  elif x == "papagaio":
    break

for y in ["a", "b", "c", "d"]:
  print(y)


for z in range(len(animais)):
  print(animais[z])


# while:

i = 0 # inicialização
while(i < 10): # condição
  print(i)
  i = i + 1 # incremento ou decremento ou controle
