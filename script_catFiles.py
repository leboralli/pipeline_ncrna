
import os, re
import config.py as CF

data = DATA_DIR
lista = os.listdir(data)
print (lista)
r = re.compile(r"^R\d{4}")
teste = []
for i in lista:
    print (i)
    chars = i[0:3]
    teste.append(chars.stripe())

print (teste)
teste2 = list(filter(r.match, teste))

print (teste2)
