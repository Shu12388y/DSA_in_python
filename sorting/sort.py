def insertingSort(n:list)->list:
    minNums = 0 
    for i in range((len(n))):
        for j in range(i+1,len(n)):
            if n[i] > n[j]:            # 2 > 4 no => 2 > 1 yes  minNums = 2  n[i] = 1 n[j] = 2 ==> [1,4,2,5] 
                minNums = n[i]
                n[i] = n[j]
                n[j] = minNums
    return n

 
print(insertingSort([13,46,24,52,20,9]))



# def mergeSort(n:list)->list:
