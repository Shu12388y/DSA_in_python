def mod(n:list)->list:
    newArray = [0]*10
    temp = 0
    for i in range(len(n)):
        temp = n[i]%10
        newArray[temp]  = n[i]
    return newArray



print(mod([1,2,3,4,66,139]))