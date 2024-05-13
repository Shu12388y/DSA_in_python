# def prefix(arr,l,r):
#     sum = 0
#     for i in range(l,r+1):
#         sum = sum  + arr[i]
#     return sum


# print(prefix([2,4,5,2,3],2,4))         



def prefix_hash(arr,l,r):
    index_map={}
    sum = 0 
    for i in range(l,r+1):
        index_map[i] = arr[i] 
        sum  = sum + index_map[i]
    return sum



def prefix_array(arr,l,r):
    prefixArray = [0]*len(arr)
    for i in range(len(arr)):
        prefixArray [i] = prefixArray[i-1]+arr[i]
    return prefixArray[r]-prefixArray[l-1]    

# print(prefix_hash([2,4,5,2,3],2,4))         


print(prefix_array([2,4,5,2,3],2,4))         

