def duplicateList(l: list) -> list:
    res = []
    seen = set()
    for i in l:
        if i in seen:
            res.append(i)
        else:
            seen.add(i)
    return res

print(duplicateList([1, 1]))  # Output: [1]

# check the code
