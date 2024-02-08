# largest element in the list

def largest(l):
    for x in l:
        for y in l:
            if(y>x):
                break
            else:
                return x
    return None        

print(largest([1,2,900,3,4,0,100,120,340,10000]))