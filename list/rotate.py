def rotate(l):
    temp = l[0]
    for i in range(1,len(l)):
        l[i-1] = l[i]
    l[len(l)-1] = temp
    return l



print(rotate([10,20,30,40]))