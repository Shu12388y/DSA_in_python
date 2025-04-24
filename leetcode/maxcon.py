def findMaxCons(a:list):
    temp  = 0 
    max_count = 0
    for i in range(0,len(a)):
        if a[i] == 1:
            temp +=1
            max_count = max(max_count,temp)
        else:
            temp = 0 
    return max_count   

print(findMaxCons([1,1,0,1,1,1]))
# print(findMaxCons([1,0,1,1,0,1]))


