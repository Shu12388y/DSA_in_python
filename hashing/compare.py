from collections import defaultdict


def search(arr,brr):
    hash_map1 = defaultdict(int)
    hash_map2 = defaultdict(int)
    for i in range(len(arr)):
        hash_map1[arr[i]] = hash_map1[arr[i]]+1
    for i in range(len(brr)):
        hash_map2[brr[i]] = hash_map2[brr[i]]+1
    for i in range(max(len(hash_map1),len(hash_map2))):
        if hash_map1[i] != hash_map2[i]:
            return hash_map2    
