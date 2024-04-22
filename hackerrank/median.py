def median(arr):
    newArr = sorted(arr)
    length = len(newArr)
    return newArr[length//2]



print(median([1,2,4,6,3]))