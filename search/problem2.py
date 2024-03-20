# find the last index of the occurence

def last(arr,target):
    for i in range(len(arr)-1):
        if(arr[i]==target and arr[i]==arr[i+1]):
            return 
        
            
    return -1



print(last([10,15,20,20,20,40,40],40))