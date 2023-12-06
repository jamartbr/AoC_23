file_path = "../data/day5.txt"
with open(file_path, "r") as f:
    lines = [x.strip() for x in f.readlines()]

seeds = [int(x) for x in lines[0].split()[1:]]
nSeeds = [(seeds[i],seeds[i+1]) for i in range(0,len(seeds),2)]

maps = []
i = 1
n = -1
while i<len(lines):
    if len(lines[i]) == 0:
        i+=2
        n+=1
    else:
        if len(maps) <= n:
            maps.append([])
        maps[n].append([int(x) for x in lines[i].split()])
        i+=1

# Parte 1

s = []
for i in seeds:
    for j in maps:
        for m in j:
            if i>=m[1] and i<m[1]+m[2]:
                i = i+m[0]-m[1]
                break
    s.append(i)
print(min(s))


# Parte 2

loc = 0
seed = 0
while True not in [seed in range(s[0],s[0]+s[1]) for s in nSeeds]:
    loc += 1
    seed = loc
    for j in maps[::-1]:
        for m in j:
            if seed>=m[0] and seed<m[0]+m[2]:
                seed = seed+m[1]-m[0]
                break
print(loc)