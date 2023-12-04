import re

file_path = "../data/day4.txt"
with open(file_path, "r") as f:
    lines = f.readlines()

    p1, p2 = 0, 0
    s = []

    for line in lines:
        a = re.search("Card *([\d]{1,3}): (.*)\| (.*)", line)
        n, l1, l2 = int(a.group(1)), set(a.group(2).split()), set(a.group(3).split())

        # Parte 1
        l = l1 & l2
        p1 += (2**(len(l)-1) if len(l)>0 else 0)

        # Parte 2                
        try:
            s[n-1] += 1
        except:
            s.append(1)

        for i in range(n, min(len(l)+n,len(lines))):
            try:
                s[i] += s[n-1]
            except:
                s.append(s[n-1])

    print(p1)
    print(sum(s))