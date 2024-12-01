def triList(L1):
    L1.sort()
    return L1

def calculDistance(x,y):
    x = int(x)
    y = int(y)
    return abs(x-y)


def puzzle(L1,L2):
    L1 = triList(L1)
    L2 = triList(L2)
    
    res = []
    
    for i in range(len(L1)):
        x = calculDistance(L1[i], L2[i])
        res.append(x)
    
    return res

def calculDistanceTotale(L):
    _somme = 0
    for i in L:
        _somme = _somme + i
    return _somme

file = open(r"C:\Users\jules\Documents\Cours Semestre 7\advent of code\txtJour1.txt","r")
content = file.read()
content = content.split()
file.close()


def createList(content):
    left = []
    right = []
    for i in range (len(content)):
        if(i % 2 == 0):
            left.append(int(content[i]))
        else:
            right.append(int(content[i]))
    return left,right

L1,L2 = createList(content)


def calculateSimilarity(L1,L2):
    sim = []
    for i in range(len(L1)):
        x = L1[i]
        sim.append(x*L2.count(x))
    return sim

print(calculDistanceTotale(calculateSimilarity(L1, L2)))



#print(calculDistanceTotale(puzzle(L1, L2)))





