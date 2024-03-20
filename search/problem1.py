# find the index of the first occurence of the array element

def first(l,target):
    for i in range(len(l)-1):
        if(l[i]==target):
            return i
    else:
        return -1



print(first([1,2,3,2,4,4,],2))            