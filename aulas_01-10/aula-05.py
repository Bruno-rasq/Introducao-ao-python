strg = "Hello World"

print(strg[0]) #print o H
print(strg[0:4]) #print do indice 0 ao 4
print(strg[0:4:2]) #print do indice 0 ao 4 pulando de 2 em 2

print(len(strg)) #print o tamanho da string

print(strg.lower())
print(strg.upper())
print(strg.strip()) #remove os espaços em branco no inicio e no fim da string

print(strg.replace("Hello", "Bom dia"))

a = strg.split(" ")
b = " ".join(a)

print(a)
print(b)

frase = "Ao brincar de xadrez, você pode jogar quinze tipos de aberturas, desde a defesa espanhola até a zukertort."

print(frase.find("xadrez"))

if "xadrez" in frase:
  print("a frase contem xadrez")