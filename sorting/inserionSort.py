def insertionSort(n:list):
    for i in range(0,len(n)):
        if n[0] > n[i]:
            n[0],n[i] = n[i],n[0]
        for j in range(1,len(n)-1):
            if n[j] > n[j+1]:
                n[j],n[j+1] = n[j+1],n[j]
    return n            


print(insertionSort([10,1,4,3,2]))
