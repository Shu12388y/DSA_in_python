def removeZeros(arr):
        newArray =[]
        count = 0
        if len(arr) == 2 and arr[0] != arr[1]:
            return arr
            
        for i  in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                arr[i] = arr[i]*2
                arr[i+1] = arr[i+1]*0
        for i in range(len(arr)):
            if arr[i] != 0:
                newArray.append(arr[i])
            if arr[i] == 0:
                count += 1
        for i in range(count):
            newArray.append(0)
        return newArray
         
                





# print(arrayCheck([847,847,0,0,0,399,416,416,879,879,206,206,206,272]))
# print(arrayCheck([1,2,2,1,1,0]))
# print(arrayCheck([1,0]))


print(removeZeros([1,2,2,1,1,0]))
print(removeZeros([847,847,0,0,0,399,416,416,879,879,206,206,206,272]))
print(removeZeros([1,0]))
print(removeZeros([2,2]))







