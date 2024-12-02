L = [7,6,4,2,1]
L1 = [1,2,7,8,9]
L2 = [9,7,6,2,1]
L3 = [1,3,2,4,5]
L4 = [8,6,4,4,1]
L5 = [1,3,6,7,9]

def checkOrder(L):
    increasing = False
    decreasing = False
    if(L[0] < L[1]):
        increasing = True
    elif (L[0] > L[1]):
        decreasing = True
    else:
        return False,False
    
    return increasing,decreasing



def checkReport(L):
    
    increasing,decreasing = checkOrder(L)
    
    res = False
    
    for i in range(len(L)-1):
        if(increasing and L[i] < L[i+1]):
            if(L[i+1] >= L[i]+1 and L[i+1] <= L[i] + 3):
                res = True
            else : 
                return False
        elif(decreasing and L[i] > L[i+1]):

            if(L[i+1] <= L[i]-1 and L[i+1] >= L[i] - 3):
                res = True
            else : 
                return False               
        else:
            return False
    return res




def checkReportUpdate(L):
    increasing,decreasing = checkOrder(L)
    
    res = False
    
    for i in range(len(L)-1):
        if(increasing and L[i] < L[i+1]):
            if(L[i+1] >= L[i]+1 and L[i+1] <= L[i] + 3):
                res = True
            else :
                L.remove(L[i])
                if(checkReport(L)):
                    return True
                else:
                    return False
        elif (increasing and L[i] >= L[i+1]):
            L.remove(L[i])
            if(checkReport(L)):
                return True
            else:
                return False
            
        elif(decreasing and L[i] > L[i+1]):

            if(L[i+1] <= L[i]-1 and L[i+1] >= L[i] - 3):
                res = True
            else : 
                L.remove(L[i])
                if(checkReport(L)):
                    return True
                else:
                    return False  
        elif (decreasing and L[i] <= L[i+1]):
            L.remove(L[i])
            if(checkReport(L)):
                return True
            else:
                return False
        else:
            return False
    return res

def checkReportFile(L):
    res = 0
    
    for i in range(len(L)):
        x = L[i].split()
        x = [ int(y) for y in x]
        if(checkReportUpdate(x)):
            res += 1
    return res

file = open(r"C:\Users\jules\Documents\Cours Semestre 7\advent of code\adventOfCode2024\jour2Input.txt","r")
with file as f:
    alist = [line.rstrip() for line in f]
file.close()

print(checkReportFile(alist))

    
    