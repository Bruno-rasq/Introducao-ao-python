# metodos e manipulação de strings.

frase = "frase aleatoria em python"

result = "python" in frase #verificar se a variavel frase contem a string python

print(result)

result2 = "python" not in frase #verificar se a variavel frase não contem a string python

print(result2)

frase2 = "frase aleatoria em PYTHON"
key = "python"

response = key.upper() in frase2.upper()

print(response)

data = "texto aleatorio"
data2 = " texto aleatorio 2"

responseData = data + data2 #concatenação de strings

print(responseData)

dia = "27"
mes = "03"
ano = 2024

date = dia + "/" + mes + "/" + str(ano) #operação de casting
date2 = "{}/{}/{}"

print(date)
print(date2.format(dia, mes, ano))

# metodo format vai substituir no templete as variaveis passadas como parametrs