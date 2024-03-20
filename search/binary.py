def binarySearch(l,target):
    low = 0
    high = len(l)-1
    while low<=high:
        mid = (low+high)//2
        if(l[mid]==target):
            return 1
        elif(l[mid] < target):
            low = mid+1    
        else:
            high = mid-1
    return -1



print(binarySearch([1,2,3,5,4],5))    


