def maxNumber(arr):
    maxArray = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == 0:
                maxArray.append(arr[i])
                maxArray.append(arr[j]) 
    if len(maxArray)>0:
        return max(maxArray)
    else:
        return -1




print(maxNumber([-10,8,6,7,-2,-3]))

