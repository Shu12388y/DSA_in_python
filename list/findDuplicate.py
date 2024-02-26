def find(l):
    for j in range(0,len(l)-1):
        for i in range(j+1,len(l)):
            temp = l[j]
            if temp == l[i]:
                return True
    else:
        return False    


# print(find([2,14,18,22,22]))                

# good for small size arrays


# let's Optimise it






