# A = [10,6,4,5,1]


def stone(a:list,h):
    k = 1
    totalStone = sum(a) 
    while(True):
        if int(totalStone/k) <= h:
            break
        else:
            k += 1
    print(k)


stone([10,6,4,5,1],9)    

