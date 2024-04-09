def findFrequency(arr,n):
    count = 0
    for i in range(1,len(arr)):
        if(arr[i]==n):
            count = count+1
    return count




print(findFrequency([1,2,3,4,2,2,4,3],9))

