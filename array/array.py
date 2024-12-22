# arr[] = {2,5,1,3,0}


def largest(a:list):
    temp = a[0]
    for i in range(1,len(a)):
        if temp < a[i]:
            temp = a[i]
            i = i+1
    print(temp)



# largest([2,5,1,3,0])




# def secondlargest(a:list):
#     temp = a[0] + 1
#     for i in range(1,len(a)):
#         if temp in a:
#             temp =  a
#         else:
#             temp = a[i]
#     print(temp)


# secondlargest([1,2,4,7,7,5])




# def secondlargest(a:list):
#     temp1 =  a[0]
#     temp2 = a[0]
#     for i  in range(1,len(a)):
#         if temp1 > a[i]:
#             temp1 = a[i]
#         if temp2  <  a[i]:
#             temp2 = a[i]
#     for i in range(len(a)):
#         if temp1 > a[i]:
#             temp1 = a[i]
#         if temp2 > a[i]:

#     print(temp1,temp2)

# secondlargest([1,2,4,7,7,5])





# def isSorted(a:list):
#     res = False
#     for i in range(0,len(a)-1):
#         if a[i]+1 !=  a[i+1]:
#             break
#     else:
#         res = True
#     print(res)
    


# isSorted([1,2,3,6,4,5])



def isSorted(a:list):
    res = False
    for i in range(1,len(a)):
        if a[i-1] > a[i]:
            break
    else:
        res =  True
    print(res)


isSorted([1,2,3,4,5])
            