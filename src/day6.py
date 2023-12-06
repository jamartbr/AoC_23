from functools import reduce

file_path = "../data/day6.txt"
with open(file_path, "r") as f:
    lines = f.readlines()

t1 = [int(x) for x in lines[0].split()[1:]]
d1 = [int(x) for x in lines[1].split()[1:]]
t2 = int("".join([str(x) for x in t1]))
d2 = int("".join([str(x) for x in d1]))
p1 = []
p2 = 0


# Parte 1

for i in range(len(t1)):
    p1.append(0)
    for j in range(t1[i]):
        if j*(t1[i]-j)>d1[i]:
            p1[i] += 1
 
p1 = reduce((lambda x, y: x * y), p1)           
print(p1)


# Parte 2

for j in range(t2):
    if j*(t2-j)>d2:
        p2+=1
         
print(p2)