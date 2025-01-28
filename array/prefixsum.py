# brute force approach for prefix sum
def prefixSum(a:list):
    prefix = [0]*len(a)
    prefix[0] = 0
    temp = 0
    for i in range(len(a)):
        temp += a[i]
        prefix[i] = temp
    print(prefix)

prefixSum([-4,-3,-2,-1,4,3,2])