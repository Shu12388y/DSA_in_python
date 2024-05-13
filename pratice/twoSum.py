def twoSum(arr,target):
    index_map={}
    for i in range(len(arr)):
        index_map[arr[i]] = i
    for i in range(len(arr)):
        diff = target - arr[i] 
        if diff in index_map:
            return [i,index_map[diff]]
    else:
        return -1                    
        


print(twoSum([2,7,11,15],9))            