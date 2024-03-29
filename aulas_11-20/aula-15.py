import os

os.system("clear")

#Lambda 

'''
Lambda é uma função anônima, ou seja, uma função sem nome.
'''

s = lambda a, b: a + b
print(s(2, 3))
print(s(2, 3))


F = lambda x, fun: x + fun(x)
r = F(2, lambda x: x*x)
print(r)

# F é a mesma coisa que FuncF

def mul(x):
  return x*x

def soma(x, y):
  return x + y

def FuncF(x):
  return x + mul(x)
