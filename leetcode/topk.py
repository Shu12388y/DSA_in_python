def findTopK(a:list,k:int):
    freq = {}
    res = []
    for i in range(len(a)):
        if a[i] not in freq:
            freq[a[i]] =  1
        else:
            freq[a[i]] += 1
    for i in freq:
        if freq[i] >= 2:
            res.append(i)
    print(res)


findTopK([1,1,1,2,2,3,4],2)