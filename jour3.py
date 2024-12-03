import re

file = open(r"C:\Users\jules\Documents\Cours Semestre 7\adventofCode\adventOfCode2024\jour3Input.txt","r")
content = file.read()
file.close()

text = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

x = re.findall("mul\([0-9]*,[0-9]*\)", content)


def calculateMul(textRegex):

    res = 0
    for i in range(len(x)):
    
        y = re.findall("mul\(([0-9]*,[0-9]*)\)",x[i])
        for j in range(len(y)):       
            y[j] = y[j].split(",")
            y[j][0] = int(y[j][0])
            y[j][1] = int(y[j][1])
            res = res + y[j][0] * y[j][1]
            
    return res

print(calculateMul(x))
            