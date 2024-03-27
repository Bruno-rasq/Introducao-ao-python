# boolean em python

'''
tipo boolean são tipos de dados que guardam informações de verdadeiro ou falso
no caso True ou False, com a primeira letra maiuscula.

'''

ligado = True

print(ligado)

'''
há tambem outras formas de se receber um retorno booleano, como por exemplo expressões logicas 

10 > 5, retorno True
10 < 5, retorno False

'''

#strings vazias retornam False?

test = ""
print(bool(test)) # ué 

if test:
  print("strign teste não está vazia")
else:
  print("string teste está vazia")

# uqaleur valor diferente de 0 retorna True, senão False