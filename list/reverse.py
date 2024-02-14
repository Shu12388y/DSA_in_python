def reverse_list(l):
    newlist = list()
    for i in range(len(l)):
        newlist.append(l[len(l)-i-1])
    return newlist    
# time complexity O(n)


print(reverse_list([11,2,3,4,5,0,87,4]))