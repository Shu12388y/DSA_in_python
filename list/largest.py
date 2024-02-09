# largest element in the list

# def largest(l):
#     for x in l:
#         for y in l:
#             if(y>x):
#                 break
#             else:
#                 return x
#     return None        

# print(largest([1,2,900,3,4,0,100,120,340,10000]))


def findLargest(l):
    large = sorted(l)
    return large[-1]


print(findLargest([1,90, 3,4,7,19,76]))




# find the number 

num = 0
def find(l):
    for i in l:
        if l[i] > l[i+1]:
            num  = l[i]
    return num            


print(find([1,2,3,4]))