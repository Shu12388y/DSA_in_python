# find the second largest
#  1.first find the largest element
#  2. compare the lragest element with other elements


def secondLargest(l):
    if len(l)<=1:
        return None
    lar=getMax(l)
    slar=None
    for i in l:
        if i!=lar:
                if slar == None:
                        slar=i
                else:
                        slar = max(slar,i)



def getMax(l):
    res =l[0]
    for i in range(1,len(l)):
        res = max(res,l[i])
    return res


print(secondLargest([1,2,3,4]))    