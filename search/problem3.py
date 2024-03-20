# count the number of occurence

def first(arr,target):
    for i in range(len(arr)-1):
        if(arr[i] == target and arr[i] == arr[i+1] ):
            return i
    else:
        return -1



def last(arr,target):
    for i in range(len(arr)-1):
        if(arr[i]==target and arr[i]==arr[i+1]):
            return i+1
    else:
        return -1        

def count(arr,target):
    
    f = first(arr,target)
    if(f == -1):
        return 0
    else:
        return last(arr,target)-first(arr,target)+1

      




print(count([10,20,20,20,40,40],20))