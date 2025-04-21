prevcount = 0
def findMaxCons(a:list):
    count = 0
    for i in range(0,len(a)):
        if a[i] == 1:
            count +=1
            prevcount = count
        else:
            count = 0
    if prevcount > count:
        return prevcount
    else:
        return count

print(findMaxCons([1,1,0,1,1,1]))
print(findMaxCons([1,0,1,1,0,1]))


