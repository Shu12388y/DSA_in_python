def merge(l1,l2):
    l = list()
    return sorted(l1+l2)



print(merge([1,2,3],[2,3,4]))


# merge sorted array



def newMerge(l1,l2):
    l = list()
    for i in range(0,len(l1)):
        l.append(l1[i])
    for i in range(0,len(l2)):        
        l.append(l2[i])
    return sorted(l)



print(newMerge([1,2,4,5,6],[1,2,3,4]))