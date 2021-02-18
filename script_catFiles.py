import os, re
# import config.py

#Verificando se os diretórios existem
dir_data = "/home/boralli/workdir/data"
if os.path.isdir(dir_data):
    data = dir_data
else:
    data = "/homelocal/boralli/workdir/data"

#Extraindo apenas IDs
lista = os.listdir(data)

r = re.compile(r"^(R\d{4})")
samples_lista = [x for x in lista if re.search(r, x)] #usando lambda
# print (samples_lista)

IDs = []
for i in samples_lista:
    sliced = i[:5]
    # print (sliced)
    IDs.append(sliced)

# print (IDs)
unique = list(dict.fromkeys(IDs))
print (unique)
for i in unique:
    itensUnicos = re.match(i, str(samples_lista))
    print (itensUnicos)
# sample = [x for x in unique if re.search(unique,x)]
# print (sample)
