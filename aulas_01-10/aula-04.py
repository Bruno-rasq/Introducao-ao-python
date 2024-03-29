import random

#importando biblioteca random 

num_i = 10
num_f = 10.0
num_c = 10 + 0j

num_i_2 = int(num_f) #parse de float para int

num_f_2 = float(num_i) #parse de int para float

num_to_strg = str(num_i) #parse de int para string

strg_to_num = int(num_to_strg)

rand = random.randint(0, 10)
rand_range = random.randrange(0, 10)

# # random.randint(a, b) retorna um numero inteiro entre a e b

print(rand)
print(rand_range)