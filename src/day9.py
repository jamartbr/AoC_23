def reducir(line):
    if len(line)==0:
        return 0
    
    aux = []
    for i in range(len(line)-1):
        aux.append(line[i+1]-line[i])

    return line[-1]+reducir(aux)

file_path = "../data/day9.txt"
with open(file_path, "r") as f:
    lines = f.readlines()

p1,p2 = 0,0
for line in lines:
    line = [int(x) for x in line.strip().split()]
    p1 += reducir(line)
    p2 += reducir(line[::-1])

print(p1)
print(p2)
    
    

