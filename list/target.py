# list [1,2,3,4,5]
# target = 3
# return [0,1]


# leetcode Two sum done

# time Complexity O(n*n)

def targetList(l,target):
    if(len(l)<0):
        return None
    else:
        for j in range(0,len(l)-1):
            for i in range(j+1,len(l)):
                temp = l[j]
                if l[i]+temp == target:
                    return [j,i]
            


                # 0 1 2 3 4 5 6
print(targetList([1,2,3,5,6,3,5],10))            