def mergeString(l1:str,l2:str):
    res=""
    for i in range(len(l1)):
        res = res + l1[i]
        res = res + l2[i]
    print(res)


mergeString("abd","pqr")

