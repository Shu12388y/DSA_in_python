def grade(arr):
    newArray=[0]*len(arr)
    for i in range(len(arr)):
        c = arr[i]
        if(c<38):
            newArray[i] = c
        elif (c+1)%5 == 0:
            newArray[i] = c+1
        elif (c+2) % 5 == 0:
            newArray[i] = c+2
        else:
            newArray[i] = c
    return newArray        





print(grade([73,67,38,33]))
# def gradeTest(n):
#     if(n<38):
#         return n
#     elif (n+1) % 5 == 0:
#         return n+1
#     elif (n+2) % 5 == 0:
#         return n+2
#     else:
#         return n




# print(gradeTest(67))             

