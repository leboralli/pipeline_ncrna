import os, re
# import config.py

#Verificando se os diretórios existem
dir_data = "/home/boralli/workdir/data"
if os.path.isdir(dir_data):
    data = dir_data
else:
    data = "/homelocal/boralli/workdir/data"

lista = os.listdir(data)
# print (lista)
r = re.compile(r"^(R\d{4})")
samples_lista = list(filter(r.findall, lista))
print (samples_lista)
# teste = []
# for i in lista:
#     print (i)
#
#     teste.append(chars.stripe())

# print (teste)
# teste2 = list(filter(r.match, teste))

# print (teste2)
