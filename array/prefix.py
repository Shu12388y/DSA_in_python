# prefix sum
# brute force solution
def prefix(l:list)->list:
    prefixList = [0]*len(l)
    temp = 0 
    for i in range(len(l)):
        temp = temp + l[i]
        prefixList[i] = temp
    print(prefixList)

# prefix([2,3,7,5])





def prefixhash(l:list)->list:
    prefixSum = [0]*len(l)
    prefixSum[0] = l[0]
    for i in range(1,len(l)):
        prefixSum[i] = prefixSum[i-1] + l[i]
    print(prefixSum) 



prefixhash([2,3,7,5])