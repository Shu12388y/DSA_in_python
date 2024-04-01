def minmax(arr):
    sum1 =0
    sum2 = 0
    sortedList = sorted(arr)
    firstElement = sortedList[0]
    lastElement = sortedList[len(arr)-1]
    for i in range(1,len(arr)-1):
        sum1 = sortedList[i]+sum1
        sum2 = sortedList[i] + sum2

    print(sum1+firstElement,sum2+lastElement)




print(minmax([1,2,3,4]))
