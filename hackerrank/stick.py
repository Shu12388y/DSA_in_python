def stick(arr):
    newArray=arr
    minNumber = min(newArray)
    # print(minNumber)
    for i in range(len(arr)):
        arr[i] = arr[i] - minNumber
        if arr[i]>0:
            newArray.append(arr[i])
        print(newArray)




stick([5,4,4,2,2,8])    