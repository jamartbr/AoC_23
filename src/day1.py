file_path = "../data/day1.txt"
with open(file_path, "r") as f:

    # Parte 1

    s = 0

    lines = f.readlines()
    for line in lines:
        aux = [*filter(lambda x: x.isdigit(), line)]
        s+=int(aux[0]+aux[-1])
    print(s)

    # Parte 2

    s = 0
    n = ["zero","one","two","three","four","five","six","seven","eight","nine","0","1","2","3","4","5","6","7","8","9"]

    for line in lines:
        a = 0
        b = 0
        _min = len(line)
        _max = -1
        for i in n:
            if line.find(i)!=-1 and _min>line.find(i):
                _min = line.find(i)
                a = n.index(i)%10
                
            if line.rfind(i)!=-1 and _max<line.rfind(i):
                _max = line.rfind(i)
                b = n.index(i)%10
        s += int(a*10+b)
    print(s)