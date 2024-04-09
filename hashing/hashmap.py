from collections import defaultdict

def hashMap(arr,n):
    hash_map = defaultdict(int)
    for i in range(0,len(arr)):
        hash_map[arr[i]] = hash_map[arr[i]]+1

    return hash_map[n]   




print(hashMap([1,2,2,4],5))
