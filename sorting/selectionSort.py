def selectionSort(n:list):
    for i in range(len(n)):
        minNums = i
        for j in range(i+1, len(n)):
            if n[j] < n[minNums]:
                minNums = j
        n[i] , n[minNums] = n[minNums], n[i]

    return n         

print(selectionSort([2,3,4,5,1,5]))
