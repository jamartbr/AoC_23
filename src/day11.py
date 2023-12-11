file_path = "../data/day11.txt"
with open(file_path, "r") as f:
    lines = [x.strip() for x in f.readlines()]

exp = []
for i in range(len(lines)):
    if "#" not in lines[i]:
        exp.append(i)

colExp = []
cols = ["".join(x) for x in list(map(list, zip(*lines)))]
for i in range(len(cols)):
    if "#" not in cols[i]:
        colExp.append(i)

lines = ["".join(x) for x in list(map(list, zip(*cols)))]

galaxias = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            galaxias.append((i,j))

p1,p2 = 0,0
for i in range(len(galaxias)):
    x_1,y_1 = galaxias[i]
    p1 += sum([abs(x_2-x_1) + abs(y_2-y_1) + len(set(colExp) & set(range(min(y_1,y_2)+1,max(y_1,y_2)))) + len(set(exp) & set(range(min(x_1,x_2)+1,max(x_1,x_2)))) for x_2,y_2 in galaxias[i+1:]])
    p2 += sum([abs(x_2-x_1) + abs(y_2-y_1) + 1000000*(len(set(colExp) & set(range(min(y_1,y_2)+1,max(y_1,y_2)))) + len(set(exp) & set(range(min(x_1,x_2)+1,max(x_1,x_2))))) for x_2,y_2 in galaxias[i+1:]])
print(p1)
print(p2)
        