def height(k,arr):
    newArray = sorted(arr)
    dose = newArray[len(newArray)-1]-k
    if dose < 0:
        return 0
    else:
        return dose 



print(height(4,[1,6,3,5,2]))    