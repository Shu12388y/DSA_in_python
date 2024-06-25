def mergeSort(m:list,n:list):
    newList = m + n
    return sorted(newList)



# print(mergeSort([2,3,4,5],[9,8,6]))



def mergeList(m:list,n:list)->list:
    res = []
    i = 0
    j = 0
    while i<len(m) and j<len(n):
        if m[i] < n[j]:
            res.append(m[i])
            i = i+1
        else:
            res.append(n[j])
            j = j+1     
    while i<len(m):
        res.append(m[i])
        i = i+1
    while j < len(n):
        res.append(n[j])
        j = j+1
    return res         

# print(mergeList([1,5,4,3],[6,9,8]))   # unsorted list

# question:  write a function that take an array as input and you have low, mid and high so you have to sort the list
#


def sortingList(a: list, low: int, mid: int, high: int):
    left = a[low:mid]
    right = a[mid+1:high]
    i = 0
    j = 0 
    k = low
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            k = k+1
            i = i+1
        else:
            a[k] = right[j]
            k += 1
            j += 1
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1
    return a                          

print(sortingList([10,15,20,11,13],0,2,4))