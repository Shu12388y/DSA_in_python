def hashMap(arr):
    hash_map = {}
    for i in range(len(arr)):
        if arr[i] in hash_map:
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    query = int(input("Enter the number: "))
    if query not in hash_map:
        return -1 
    return hash_map[query]




print(hashMap([1,2,3,4,5,1,9]))
