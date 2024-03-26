# tipos básico de dados

number = 10 #tipo number int
string = "10" #tipo string
float = 10.0 #tipo number float
boolean = True #tipo booleano

# obs: o python é uma linguagem fracamente tipada, ou seja, não é necessário declarar.

# variaveis do tipo boolean devem ser escritas com a primeira letra maiuscula

verdadeiro = True
falso = False

list = [1, 2, 3, 4, 5] #/lista ou Array
tuple = (1, 2, 3, 4, 5)

dict = { 
  #dictiomary são como os Objetos em JS
  "nome": "João",
  "idade": 25,
  "altura": 1.75
}

# print(dict["nome"])

complex = complex(2, 3) 
#complex são tipos de numbers que guardam um valor real e um imaginário

print(complex.real)
print(complex.imag)

# usa-se o type() para saber o tipo de dado

x = 10 #int
print(type(x)) #<class 'int'>

y = range(0, 10) #range sao tipos de dados que guardam uma sequencia de numeros

print(y)