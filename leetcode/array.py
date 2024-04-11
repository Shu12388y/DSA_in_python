def removeZeros(arr):
            newArray =[]
            count = 0
            if len(arr) == 2 and arr[0] == 1 and arr[1] == 0 and arr[0] != arr[1]:
                return [arr[1],arr[0] ]  
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
         
                

def applyOperations(nums):
        results = []
        zero_counts = 0
        for i in range(len(nums)-1):
            if nums[i] == 0:
                zero_counts += 1
                continue
            elif nums[i] == nums[i+1]:
                results.append(nums[i]*2)
                nums[i+1] = 0
            else:
                results.append(nums[i])
        
        results.append(nums[-1])

        for _ in range(zero_counts):
            results.append(0)
        return results



# print(arrayCheck([847,847,0,0,0,399,416,416,879,879,206,206,206,272]))
# print(arrayCheck([1,2,2,1,1,0]))
# print(arrayCheck([1,0]))


# print(removeZeros([1,2,2,1,1,0]))
# print(removeZeros([847,847,0,0,0,399,416,416,879,879,206,206,206,272]))
# print(removeZeros([1,0]))
# print(removeZeros([2,2]))
# print(removeZeros([2,1]))


print(applyOperations([1,2,2,1,1,0]))
print(applyOperations([847,847,0,0,0,399,416,416,879,879,206,206,206,272]))
print(applyOperations([1,0]))
print(applyOperations([2,2]))
print(applyOperations([2,1]))








