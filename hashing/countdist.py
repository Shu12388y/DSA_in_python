# solution

def count(n:list)->int:
    d={}
    counter = 0
    for i in range(len(n)):
        if i not in d:
            d[n[i]] = 1 
    for i in range(len(d)):
        counter = d[n[i]] + counter
    return counter    

def distCount(n:list)->int:
    return len(set(n))

def distCountlog(n:list)->int:
    res = 1 
    for i in range(1,len(n)):
        if n[i]  not in n[0:i]:
            res = res +1
    return res        


print(distCountlog([10,20,10,30,30,10]))
print(distCount([10,20,10,30,30,20]))
print(count([10,20,10,30,30,20]))

