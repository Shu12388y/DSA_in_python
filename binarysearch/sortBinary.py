# SBA (sorted Binary Array)
# [0 0 0 0 0 0 0 0 1 1]
# find the position  index
# 1. last index of 0
# 2. first index of 1


def SBA(a:list):
    l = -1
    r = len(a)
    while( l+1 < r):
        middle = int((l + r)/2)
        if a[middle] == 0:
            l = middle

        else:
            r = middle
    print(l, r)

SBA([0,0,0,0,0,1,1,1])
