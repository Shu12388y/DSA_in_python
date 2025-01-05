import math

def Search(a:list,k:int):
    flag = True
    for i in range(0,math.floor(len(a)/2)):  # Best: O(1), Avg.: O(n/2) Worst; O(n)
        if k == a[i]:
            return [i,k]
        else:
            flag = False
    if(not flag):
        for i in range(math.floor(len(a)/2),len(a)):
            if k == a[i]:
                return [i,k]
        else:
            return -1


print(Search([1,4,6,3,9,0,3,5],5))

