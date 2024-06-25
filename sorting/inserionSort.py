# def insertionSort(n:list):
#     for i in range(0,len(n)):
#         if n[0] > n[i]:
#             n[0],n[i] = n[i],n[0]
#         for j in range(1,len(n)-1):
#             if n[j] > n[j+1]:
#                 n[j],n[j+1] = n[j+1],n[j]
#     return n            


# print(insertionSort([20,5,40,60,10,30]))



def insertionSort(n: list):
    for i in range(1, len(n)):
        key = n[i]                              # key = 5  [5,20,40,60,10,30]        40                             60                  10      
        j = i - 1                               # j = 0                               1                             2                   3
        while j >= 0 and key < n[j]:            # j> =  and 5 < 20 True            j>=0 and 40 < 20  False    j>=0 and 60<40 False     j>=0 and 10<60 True
            n[j + 1] = n[j]                       # n[0+1] = n[0]   n[1] = 20                                                           n[3+1] = n[3]   n[4] = 60 
            j -= 1                                     # j = -1                                                                             j -= 1   n[2+1] = n[2]   n[3] = 40  j-=1  n[1+1] = n[1]  n[2] = 20   j-=1  n[0+1] = n[0]   n[1] = 5  false
        n[j + 1] = key                              # n[-1+1] = n[0] = 5                                                                        n[-1 + 1]  = 10
    return n

print(insertionSort([20,5,40,60,10,30]))        