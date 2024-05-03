def maxDist(arr,target):
    first = 0 
    last = 0
    for i in range(0,len(arr)):
        if(target  == arr[i]):
            first = i
            break
    for i in reversed(range(len(arr))):
        if(target == arr[i]):
            last  = i
            break 
    return last-first



print(maxDist([3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2],4))




# solution 2:
def max(arr,n):
    mp = {}  
    maxDict = 0
    for i in range(n): 
        if arr[i] not in mp.keys(): 
            mp[arr[i]] = i  
        else: 
            maxDict = max(maxDict, i-mp[arr[i]]) 
  
    return maxDict 