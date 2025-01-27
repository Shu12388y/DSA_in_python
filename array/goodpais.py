# def findGoodPairs(a:list):
#     pairs = 0
#     for i in range(0,len(a)):
#         for j in range(i+1,len(a)):
#             if a[i] == a[j]:
#                 pairs += 1
#     return pairs


# print(findGoodPairs([1,1,1,1]))
# print(findGoodPairs([1,2,3,1,1,3]))





def findGoodPair(a:list):
    freq = [0] * (len(a) +1)
    ans = 0
    for i in range(len(a)):
        ans += freq[ans[i]]
        freq[ans[i]] += 1
    return ans


findGoodPair([1,2,3,1,1,3])
