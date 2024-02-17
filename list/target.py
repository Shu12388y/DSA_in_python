# list [1,2,3,4,5]
# target = 3
# return [0,1]


def targetList(l,target):
    if(len(l)<0):
        return None
    else:
        for i in range(1,len(l)):
            if l[i]+l[i-1] == target:
                return [i-1,i]



print(targetList([1,2,3,4,5],6))            