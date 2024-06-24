def mergeSort(m:list,n:list):
    newList = m + n
    return sorted(newList)



# print(mergeSort([2,3,4,5],[9,8,6]))



def mergeList(m:list,n:list)->list:
    res = []
    for i in range(len(m)-1):
        for j in range(len(n)):
            if m[i] > n[j]:
                res.append(m[i])
                i += 1
            else:
                res.append(n[j])
                j += 1
    return res        
    
print(mergeList([1,5,4,3],[6,9,8]))



