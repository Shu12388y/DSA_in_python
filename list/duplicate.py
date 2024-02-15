def duplicate(l):
    res = 1
    for i in range(len(l)):
        if l[res-1]!=l[i]:
            l[res] = l[i]
            res+=1
    return res



print(duplicate([1,2,2,3,3,4]))