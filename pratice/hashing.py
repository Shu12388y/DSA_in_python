def hash(arr):
    hashArray = [0]*(max(arr)+1)
    for i in range(len(arr)):
        hashArray[arr[i]] = hashArray[arr[i]]+1
    query = int(input("Enter the number to be count "))
    if query > len(hashArray)+1: 
        return -1
    return hashArray[query]

print(hash([1,2,3,4,4,3,2,1,4,1,4,5,0]))

