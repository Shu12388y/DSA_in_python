def insertingSort(n:list)->list:
    minNums = 0 
    for i in range((len(n))):
        for j in range(i+1,len(n)):
            if n[i] > n[j]:
                minNums = n[i]
                n[i] = n[j]
                n[j] = minNums
    return n

 
print(insertingSort([2,4,1,5]))