'''
Pegar 10 itens da lista aleatórios e remover os mesmos da lista após
os programas.

'''

from random import seed
from random import sample
seed(12345)

lista_a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lista_b = sample(lista_a, 2)

print("Valores da lista a: ", lista_a)
print("Valore da lista b: ", lista_b)

print("Removendo itens da lista B da lista A: ")
lista_c = [x for x in lista_a if x not in lista_b]

print(lista_c)
