# list [1,2,3,4,5]
# target = 3
# return [0,1]


def targetList(l,target):
    if(len(l)<0):
        return None
    else:
        for j in range(0,len(l)-1):
            for i in range(1,len(l)):
                temp = l[j]
                if l[i]+temp == target:
                    return [i-1,i]
            



print(targetList([1,2,3],3))            