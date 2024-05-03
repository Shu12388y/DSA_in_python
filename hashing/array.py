def arrayList(arr,i,j):
    temp = 0
    for k in range(i,j+1):
        temp = temp + arr[k]
    return temp

print(arrayList([1,4,1],1,1))        





# solution 2
def sumRange(nums, l, r):
	prefix = [0] * (len(nums) + 1)
 
	for i, val in enumerate(nums):
		prefix[i + 1] = prefix[i] + val
 
	return prefix[r] - prefix[l - 1]