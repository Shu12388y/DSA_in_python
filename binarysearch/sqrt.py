# find the sqaure root of x
# sqrt(17)

def findSqrt(a):
    l = 0
    r = a+1
    step = 150
    while (step):
        step-=1
        mid = (l + r)*0.5
        if (mid * mid > a):
            r = mid 
        else:
            l = mid
    print(l)


findSqrt(17)


# 