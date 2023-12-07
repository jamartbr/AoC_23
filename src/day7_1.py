from collections import Counter

file_path = "../data/day7.txt"
with open(file_path, "r") as f:
    lines = f.readlines()

s = []
order = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
for line in lines:
    mano, apuesta = line.strip().split()
    count = Counter(mano)
    diff = len(set(mano))
    apuesta = int(apuesta)
    s.append((mano, max(count.values()), -diff, apuesta))

s.sort(key=lambda x: (order.index(x[0][0]), order.index(x[0][1]), order.index(x[0][2]), order.index(x[0][3]), order.index(x[0][4])))
s.sort(key=lambda x: (x[1],x[2]))
p1 = 0
for i in range(len(s)):
    p1 += s[i][3] * (i+1)
print(p1)
