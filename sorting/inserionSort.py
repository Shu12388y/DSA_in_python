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
        key = n[i]
        j = i - 1
        while j >= 0 and key < n[j]:
            n[j + 1] = n[j]
            j -= 1
        n[j + 1] = key
    return n

print(insertionSort([20,5,40,60,10,30]))        