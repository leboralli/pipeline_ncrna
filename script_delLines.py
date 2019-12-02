#!/usr/bin/python3
import re
import sys
file = sys.argv[1]
n = sys.argv[2]
with open(file, 'r') as f:
    L = []
    for line in f:
        line = re.sub(r'\n', r'', line)
        L.append(line)
    print('\n'.join(L[n:]))
