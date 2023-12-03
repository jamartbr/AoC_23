import re

f = ["."+line.strip()+"." for line in open("../data/day3.txt","r").readlines()]
f = ["."*(len(f[0])), *f, "."*(len(f[0]))]

n,m = len(f), len(f[0])
p1,p2 = 0,0
s = {}

i,j =1,1
while i<n:
    while j<m:
        if f[i][j].isdigit():
            inicio = j-1
            j += 1
            while f[i][j].isdigit() and j<m-1:
                j += 1
            fin = j+1
            cad = f[i-1][inicio:fin]+f[i][inicio:fin]+f[i+1][inicio:fin]
            aux = re.search(r"[^0-9.]",cad)
            if aux!=None:
                # Parte 1
                p1 += int(f[i][inicio+1:fin-1])

                # Parte 2
                x = aux.span()[0]//(fin-inicio) + i - 1
                y = aux.span()[0]%(fin-inicio) + inicio
                try:
                    a = s[(x,y)][0] * int(f[i][inicio+1:fin-1])
                    b = s[(x,y)][1] + 1
                    s[(x,y)] = (a,b)
                except:
                    s[(x,y)] = (int(f[i][inicio+1:fin-1]),1)
        
        i = i+1 if j==m-1 else i
        j = 1 if j==m-1 and i<n else j+1

print(p1)
for i in s:
    if (s[i][1]==2):
        p2 += s[i][0]
print(p2)