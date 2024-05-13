# def count(arr,k):
#     index_array ={}
#     count = 0
#     diff = 0
#     for i in range(len(arr)):
#         diff  = k  - arr[i]
#         if diff in index_array:
#             count += 1
#         else:
#             index_array[arr[i]]  = i
#     return count


# print(count([1,5,7,1],6))                




def find(arr,k):
    index_array={}
    count = 0 
    for i in range(len(arr)):
        diff =  k - arr[i]
        if diff in index_array:
            count  = count + 1
        else:
            index_array[arr[i]] = i
    return count



print(find([1,5,7,1],6)) 