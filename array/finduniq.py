def findUniq(a:list):
    res = [0] * (max(a)+1)
    for num in a:
        res[num] += 1
    for i in range(len(res)):
        if res[i] ==  1:
            return i
    
# print(findUniq([2, 3, 1, 6, 3, 6, 2]))
# print(findUniq([2, 4, 7, 2, 7]))

        
def findUnique(a:list):
    ans  = 0 
    for i in range(len(a)):
        ans  = ans ^ a[i]
    return ans


print(findUnique([2, 4, 7, 2, 7]))
