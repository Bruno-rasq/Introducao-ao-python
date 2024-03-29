# comando condicional if em python

a = True

if a:
  print("a é verdadeiro")
else:
  print("a é falso")


b = 10
c = 5

if b > c:
  print("b é maior que c")

#if ternário
idade = 20
status = "maior de idade" if idade >= 18 else "menor de idade"

#if (else if === elif)

teste = 'a'

if teste == 'x':
  print("teste == x")
elif teste =='y':
  print("teste == y")
else:
  print("teste == a")

  #opredadores de comparação

clima = "sol"
dinheiro = 50

if clima == "sol" and dinheiro >= 50:
  print("vou a praia")
elif clima != "sol" and dinheiro > 50:
  print("vou ao cinema")
elif clima != "sol" or dinheiro < 50:
  print("vou ficar em casa")

'''
    AND
  true e true = true
  true e false = false
  false e true = false
  false e false = false

    OR
  true ou false = true
  false ou true = true
  true ou true = true
  false ou false = false
    
'''
