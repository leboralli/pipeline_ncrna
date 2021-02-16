
import os, re
import config.py

data = DATA_DIR
lista = os.listdir(data)

r = re.compile("^R\d{4}")
teste = []
for i in lista:
    print (i)
    chars = i[0:3]
    teste.append(chars.stripe())

print (teste)
teste2 = list(filter(r.match, teste))

print (teste2)
