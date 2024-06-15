def removeZero(n:list):
    count = 0
    b = []
    for i in range(len(n)):
        if n[i] == 0:
            count += 1 
        else:
            b.append(i)    
    for i in range(count):
        b.append(0)
    return b             

print(removeZero([0,1,2,0,4]))