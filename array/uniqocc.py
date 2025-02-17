def findOcc(a:list):
    ans = {}
    for i in range(len(a)):
        if a[i] not in ans:
            ans[a[i]] = 1
        else:
            ans[a[i]] += 1
    return len(set(ans.values())) == len(ans)


print(findOcc([1,2,2,1,1,3]))
# print(findOcc([1,2]))
# print(findOcc([-3,0,1,-3,1,1,1,-3,10,0]))

