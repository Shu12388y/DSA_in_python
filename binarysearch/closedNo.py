# a = [1,3,,5,8,11,12]
# x  = 9
# find the closet nos in A to x


def computecloseNumber(n,x):
    if(n<=x):
        return 1
    return 0

def closetNumber(a:list,x):
    l = -1
    r =len(a)
    while ( l+1 < r):
        mid = int((l +r)/2)
        if(computecloseNumber(a[mid],x) == 1):
            l = mid
        else:
            r = mid 

    print(a[l])

closetNumber([1,3,4,5,8,11,12],9)
    

