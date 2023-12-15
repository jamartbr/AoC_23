def ejeHorizontal1(fig):
    for j in range(1,len(fig)):
        n = min(j,len(fig)-j)
        arriba = "".join(fig[j-n:j])
        abajo = "".join(fig[j:j+n][::-1])
        if arriba==abajo:
            return j
    return -1

def ejeHorizontal2(fig):
    for j in range(1,len(fig)):
        n = min(j,len(fig)-j)
        arriba = "".join(fig[j-n:j])
        abajo = "".join(fig[j:j+n][::-1])
        if sum([1 for i in range(len(arriba)) if arriba[i]!=abajo[i]])==1:
            return j
    return -1

###############################################################################

file_path = "../data/day13.txt"
with open(file_path, "r") as f:
    figuras = "".join(f.readlines()).split("\n\n")
figuras = [fig.split("\n") for fig in figuras]
figuras[-1].pop()

p1,p2 = 0,0
for fig in figuras:

    ejeh1,ejev1,ejeh2,ejev2 = 0,0,0,0

    # Buscamos eje horizontal
    ejeh1 = ejeHorizontal1(fig)
    ejeh2 = ejeHorizontal2(fig)

    # Buscamos eje vertical
    fig = list(zip(*fig))  
    fig = ["".join(x) for x in fig] 

    if ejeh1==-1:
        ejev1 = ejeHorizontal1(fig)
    if ejeh2==-1:
        ejev2 = ejeHorizontal2(fig)

    p1 += ejeh1*100 if ejeh1>0 else ejev1
    p2 += ejeh2*100 if ejeh2>0 else ejev2
print(p1)
print(p2)