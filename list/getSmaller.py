def getSmaller(x,lists):
    smallerlist=[]  
    for i in range(len(lists)):
        if(lists[i]<x):
            smallerlist.append(lists[i])
    return smallerlist



print(getSmaller(10,[8,100,20,40,3,7]))


# output: [8, 3, 7]