def hash(arr,n):
    hashedArray=[0]*51
    for i in range(0,len(arr)):
        c = arr[i]
        hashedArray[c] = hashedArray[c]+1

    print(hashedArray)
    return hashedArray[n]



print(hash([1,2,3,4,4,3,2,1,9,7],2))     