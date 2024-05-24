def seq(nums):
    count = 0
    sortedList = sorted(nums)
    index=[]
    for i in range(len(sortedList)-1):
        if sortedList[i]+1 == sortedList[i+1] or sortedList[i]==sortedList[i+1]:
            index.append(sortedList[i])        
    if len(index)==len(sortedList)-1:
        return len(index)
    else:
        return len(index)+1    


print(seq([100,4,200,1,3,2]))        