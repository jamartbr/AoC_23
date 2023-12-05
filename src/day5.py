file_path = "../data/day5.txt"
with open(file_path, "r") as f:
    lines = [x.strip() for x in f.readlines()]

seeds = [int(x) for x in lines[0].split()[1:]]

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
        # for j in range(r):
        #     dest = destStart+j
        #     source = sourceStart+j
        #     if len(maps) <= m:
        #         maps.append({})
        #     maps[m][source] = dest
        i+=1

s = []
for i in seeds:
    for j in maps:
        for m in j:
            if i>=m[1] and i<m[1]+m[2]:
                i = i+m[0]-m[1]
                break
    s.append(i)
print(min(s))