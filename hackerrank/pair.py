def pair(arr):
    from collections import Counter
    count = 0
    element_counts = Counter(arr)
    for value in element_counts.values():
        count += value // 2
    return count

print(pair([1, 2, 1, 2, 1, 3, 2]))  # Output should be 2
