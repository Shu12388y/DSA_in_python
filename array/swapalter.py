# swap alternative

def alter(a:list):
    res = a[:]
    for i in range(0,len(res)-1,2):
        res[i],res[i+1] = res[i+1],res[i]
    return res 


print(alter([1,2,7,8,5,6]))