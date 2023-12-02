import re

file_path = "../data/day2.txt"
with open(file_path, "r") as f:
    lines = f.readlines()

    p1, p2 = 0, 0

    for line in lines:
        a = re.search("Game ([\d]{1,3}): (.*)", line)
        line = re.sub("[;,]", "", a.group(2)).split()

        s = [0,0,0]
        
        for i in range(0,len(line),2):
            if (line[i+1]=="red"):
                s[0] = max(s[0], int(line[i]))
            elif (line[i+1]=="green"):
                s[1] = max(s[1], int(line[i]))
            else:
                s[2] = max(s[2], int(line[i]))

        p1 += (int(a.group(1)) if s[0]<=12 and s[1]<=13 and s[2]<=14 else 0)
        p2 += s[0]*s[1]*s[2]

    print(p1)
    print(p2)