def siguiente(lines,x,y,dirx,diry):
    if dirx==1:
        x += 1
        if lines[x][y]=='|':
            dirx = 1
            diry = 0
        elif lines[x][y]=='L':
            dirx = 0
            diry = 1
        else:
            dirx = 0
            diry = -1
    elif dirx==-1:
        x -= 1
        if lines[x][y]=='|':
            dirx = -1
            diry = 0
        elif lines[x][y]=='F':
            dirx = 0
            diry = 1
        else:
            dirx = 0
            diry = -1
    elif diry==1:
        y += 1
        if lines[x][y]=='-':
            dirx = 0
            diry = 1
        elif lines[x][y]=='J':
            dirx = -1
            diry = 0
        else:
            dirx = 1
            diry = 0
    else:
        y -= 1
        if lines[x][y]=='-':
            dirx = 0
            diry = -1
        elif lines[x][y]=='L':
            dirx = -1
            diry = 0
        else:
            dirx = 1
            diry = 0
    
    return x,y,dirx,diry

###############################################################################

file_path = "../data/day10.txt"
with open(file_path, "r") as f:
    lines = [x.strip() for x in f.readlines()]
n = len(lines)
m = len(lines[0])

for i in range(n):
    if lines[i].find('S')!=-1:
        x = i
        y = lines[i].find('S')
        break

dirx, diry = 0, 0

if lines[x][y+1] in '-J7':
    diry = 1
elif lines[x][y-1] in '-LF':
    diry = -1
elif lines[x+1][y] in '|LJ':
    dirx = 1
else:
    dirx = -1

casillas = [(x,y)]

x,y,dirx,diry = siguiente(lines,x,y,dirx,diry)
casillas.append((x,y))
while lines[x][y]!='S':
    x,y,dirx,diry = siguiente(lines,x,y,dirx,diry)
    casillas.append((x,y))

print((len(casillas)-1)//2)

###############################################################################

# Parte 2

s = 0
for i in range(n):
    dentro = False
    for j in range(m):
        if (i,j) in casillas and lines[i][j] in "|JL":
            dentro = not dentro
        elif dentro and (i,j) not in casillas:
            s += 1
print(s)