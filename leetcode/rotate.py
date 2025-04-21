def rotate(a:list,k:int):
    for i in range(0,k):
        temp = a.pop()
        a.insert(0,temp)
    print(a)

def rotates(nums,k):
    k = k % len(nums)
    nums[:] = nums[::-1]
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
    print(nums)

rotate([1,2,4,5],2)
rotates([1,2,4,5],2) 
