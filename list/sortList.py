def checkSort(l):
    if len(l) < 2:
        return True  
    i = 1 
    while i < len(l):
        if l[i] < l[i-1]:
            return False
        i += 1
    return True
      

            
# using sorted function

def sorted(l):
    sl == sorted(l)
    if(sl==l):
        return True
    return False    

print(checkSort([1,2,3,4]))
