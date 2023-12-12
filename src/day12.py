import functools

@functools.cache
def getPosibles(line,nums,i):
    # Caso imposible
    if (len(line)==0 or i>=len(line)) and len(nums)>0:
        return 0
    if len(nums)==0 and "#" in line:
        return 0
    
    # Caso base
    if len(nums)==0:
        return 1
    
    # Caso recursivo
    if line[i]=='?':
        return getPosibles(line[:i]+"#"+line[i+1:],nums,i)+getPosibles(line[:i]+"."+line[i+1:],nums,i)
    
    if line[i]=='.':
        return getPosibles(line[1:],nums,i)
    
    n = int(nums.split(',')[0])
    if line[:n]=="#"*n and (n>=len(line) or line[n]!="#"):
        line = '.'+line[n+1:]
        nums = ",".join(nums.split(',')[1:])
        return getPosibles(line,nums,0)
    elif line[:n]=="#"*n and line[n]=="#":
        return 0
    elif "#" in line[:n] and "." in line[:n]:
        return 0
    else:
        return getPosibles(line,nums,i+1)


###############################################################################

file_path = "../data/day12.txt"
with open(file_path, "r") as f:
    lines = [x.strip() for x in f.readlines()]

nums = []
for i in range(len(lines)):
    lines[i], n = lines[i].split()
    nums.append(n)

# Parte 1
p1 = 0
for i in range(len(lines)):
    p1 += getPosibles(lines[i], nums[i], 0)
print(p1)

# Parte 2
for i in range(len(lines)):
    lines[i] = "?".join([lines[i] for j in range(5)])
    nums[i] = ",".join([nums[i] for j in range(5)])

p2 = 0
for i in range(len(lines)):
    p2 += getPosibles(lines[i], nums[i], 0)
print(p2)

