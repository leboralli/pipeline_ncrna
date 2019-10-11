import random, os

n = 10000

for i in range(n):
    file = "amostra_" + str(random.randrange(1,100000)) + str(random.choice([".fastq", ".BAM"]))
    # command = "echo $file"
    os.system('touch files/' + file)
