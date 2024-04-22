def validPair(k, arr):
    newArray = []
    for i in range(0, len(arr)):
        c = arr[i]
        for j in range(i + 1, len(arr)):  
            if (c + arr[j]) % k == 0:  
                newArray.append(c + arr[j])
    return len(newArray)



print(validPair(3,[1,3,2,6,1,2]))                