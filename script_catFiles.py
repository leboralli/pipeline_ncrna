
import os
# import config.py

data = DATA_DIR
lista = os.listdir(data)

teste = []
for i in lista:
    chars = i[0:3]
    teste.append(chars)

print (teste)
