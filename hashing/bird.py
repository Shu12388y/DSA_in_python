from collections import defaultdict

def bird(b):
    hash_map = defaultdict(int)
    for i in range(len(b)-1):
        hash_map[b[i]] = hash_map[i]+1
    return max(hash_map)-1



print(bird([1 ,4 ,4 ,4 ,5 ,3]))             
