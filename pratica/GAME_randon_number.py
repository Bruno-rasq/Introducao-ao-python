import random
import os

erros=0
n_sorteado = random.randrange(0,100)
jogador = int(input("Digite um número: "))

while jogador != n_sorteado:
  os.system('clear')
  if n_sorteado > jogador:
    print("O número sorteado é maior")
  elif n_sorteado < jogador:
    print("O número sorteado é menor")
  erros += 1
  jogador = int(input("Digite um número: "))

print(f"Você acertou em {erros} tentativas, valor sorteado {n_sorteado}")