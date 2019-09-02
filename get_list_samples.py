import os
import subprocess

samples = []
subprocess.check_output("ls | grep -Po '.{28}' | uniq > samples.txt",shell=True)

with open("samples.txt") as inputfile:
    for line in inputfile:
        samples.append(line.strip())
