from collections import defaultdict


def dictArray(arr):
    hash_map = defaultdict(int)
    for i in arr:
        hash_map[i] += 1

    return hash_map



print(dictArray([1,2,1,2,4,5,5]))        