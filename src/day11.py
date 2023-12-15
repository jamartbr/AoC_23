file_path = "../data/day11.txt"
with open(file_path, "r") as f:
    lines = [x.strip() for x in f.readlines()]

filasVacias = [i for i, fila in enumerate(lines) if '#' not in fila]
colVacias = [i for i, col in enumerate(list(map(list, zip(*lines)))) if '#' not in col]

galaxias = [(i,j) for i in range(len(lines)) for j in range(len(lines[i])) if lines[i][j] == "#"]

p1,p2 = 0,0
for k in range(len(galaxias)):
    x_1,y_1 = galaxias[k]
    for x_2,y_2 in galaxias[k+1:]:
        for i in range(min(x_1,x_2),max(x_1,x_2)):
            p1 += 2 if i in filasVacias else 1
            p2 += 1000000 if i in filasVacias else 1
        for j in range(min(y_1,y_2),max(y_1,y_2)):
            p1 += 2 if j in colVacias else 1
            p2 += 1000000 if j in colVacias else 1
print(p1)
print(p2)
        