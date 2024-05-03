def maxNumber(arr):
    maxArray = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == 0:
                maxArray.append(arr[i])
                maxArray.append(arr[j]) 
    if len(maxArray)>0:
        return max(maxArray)
    else:
        return -1




print(maxNumber([-10,8,6,7,-2,-3]))



def maxTest(arr):
    set_Nums = list(arr)
    k = -1
    for n in set_Nums :
        if n > 0:
            if n > k and -n in set_Nums:
                k = n 

    return k



print(maxTest([-10,8,6,7,-2,3]))
