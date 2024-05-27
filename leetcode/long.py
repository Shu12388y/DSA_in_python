def long(nums:list)->int:
    # sortedList = set(sorted(nums))
    numsList = list(set(sorted(nums)))
    print(numsList)
    for i in range(len(numsList)-1,0,-1):
        if numsList[i] != numsList[i-1]+1:
            numsList.pop(i)  
    return(len(numsList))         
    


print(long([0,3,7,2,5,8,4,6,0,1,100,-1]))