def removeDuplicate(l):
    for i in range(len(l)    ):
        if l[i] == l[i-1]:
            l.remove(l[i-1])
    return l


print(removeDuplicate([1,2,2,3,3,4]))    