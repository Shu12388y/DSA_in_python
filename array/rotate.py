# [1,2,3,4,5] k =2
# [5,4,1,2,3]

def rotateArr(a:list,k:int):
    temp  = []
    for i in range(len(a) - k,len(a)):
        temp.append(a[i])
    for i in range(0, len(a)-k):
        temp.append(a[i])
    a = temp[:]
    print(a)

# rotateArr([1,2,3,4,5],2)   



def rotateInPlace(a:list,k:int):
    for i in range(0,len(a)//2):
        a[i] , a[len(a)-1 - i] = a[len(a)-1 - i] , a[i]
    a[:] = a[:k]
    
    print(a)


rotateInPlace([1,2,3,4,5],2)   
