def largest(a):
    if len(a) == 1:
        return a[0]
    else:
        for i in range(len(a)):
            res=1
            if a[res-1]!= a[i]:
                a[res] =a[i]
                res+=1
    return res



print(largest([0 ,0 ,1 ,2 ,1]))                    