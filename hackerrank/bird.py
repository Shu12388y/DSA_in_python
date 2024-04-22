def bird(arr):
    newArray = []
    count = 0
    sortedArray = sorted(arr)
    for i in range(len(sortedArray)):
        c = sortedArray[i]
        # print(sortedArray)
        if sortedArray[i] == c:
            count += 1
        print(count)
        newArray.append(count)
    return newArray        


print(bird([1,4,4,4,5,3]))

