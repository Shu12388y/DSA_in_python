# largest element in the list

def largest(l):
    for x in l:
        for y in l:
            if(y>x):
                break
            else:
                return x
    return None        

# print(largest([1,2,900,3,4,0,100,120,340,10000]))


def findLargest(l):
    large = sorted(l)
    return large[-1]


# print(findLargest([1,90, 3,4,7,19,76]))




# find the largest number 

def findMax(l):
    if not l:
        return None
    else:
        for x in l:
            for y in l:
                if y > x:
                    break
            else:
                return x    
    return None                





def findmax(l):
    if not l:
        return None
    else:
        res = l[0]
        for x in range(1,len(l)):
            if l[x] > res:
                res = l[x]
    return res



print(findmax([1,2,5,6,7,3]))



