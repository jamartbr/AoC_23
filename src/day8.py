import re
from functools import reduce
from math import gcd  

def Parte1(grafo, cont):
    actual = "AAA"
    while actual != "ZZZ":
        if instruc[cont%len(instruc)] == "L":
            actual = grafo[actual][0]
        else:
            actual = grafo[actual][1]
        cont += 1
    return cont

def Parte2(inicio, grafo, cont):
    c = 0
    actual = inicio
    while actual[2] != "Z":
        if instruc[(c+cont)%len(instruc)] == "L":
            actual = grafo[actual][0]
        else:
            actual = grafo[actual][1]
        c += 1
    return c

###############################################################################

file_path = "../data/day8.txt"
with open(file_path, "r") as f:
    lines = f.readlines()

instruc = lines[0].strip()

grafo = {}
for line in lines[2:]:
    nodos = re.match(r"([\dA-Z]{3}) = \(([\dA-Z]{3}), ([\dA-Z]{3})\)",line)
    grafo[nodos.group(1)] = [nodos.group(2),nodos.group(3)]

c = 0
c = Parte1(grafo, 0)
print(c)

s = []
for n in grafo:
    if n[2]=="A":
        aux = Parte2(n, grafo, c)
        s.append(aux)
        c += aux
print(s)

s = reduce((lambda x,y:int(x*y/gcd(x,y))), s) # minimo comun multiplo
print(s)