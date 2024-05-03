sample_Array =[1,2,3,4,5]
def hashedArray(arr):
    hashingArray =[0]*(max(arr)+1)
    for i in arr:
        hashingArray[i] += 1
    return hashingArray


print(hashedArray(sample_Array))        