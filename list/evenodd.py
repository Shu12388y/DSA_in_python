def separtor(lists):
    even=[]
    odd=[]
    for i in range(len(lists)):
        if(lists[i]%2==0):
            even.append(lists[i])
        else:
            odd.append(lists[i])    
    return even,odd



print(separtor([1,2,3,4]))