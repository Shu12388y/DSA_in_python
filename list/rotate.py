def rotate(l,d):
    temp = l[0]
    for j in range(0,d):
        for i in range(1,len(l)):
            l[i-1] = l[i]
        l[len(l)-1] = temp
    return l



print(rotate([1,2,3,4,5],4))