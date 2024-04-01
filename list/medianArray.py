def medianOfTwoArray(list1,list2):
    mergeArray = list1 + list2
    sortedArray=sorted(mergeArray)
    if len(sortedArray)%2==0:
        right = len(sortedArray)//2
        left = right -1
        return (sortedArray[right]+sortedArray[left]) / 2.0
    else:
        return sortedArray[len(sortedArray)//2]



print(medianOfTwoArray([1,3],[2]))