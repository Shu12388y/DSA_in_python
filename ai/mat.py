# def mat(a:list):
#     res = {}
#     result = False
#     for i in range(0,len(a)):
#         for j in range(0,len(a)):
#            if a[i][j] in res:
#             res[a[i][j]] += 1
#            else:
#                 res[a[i][j]] =  1
#     for i in res:
#         if res[1] == res[i]:
#             result = True
#         else:
#             result = False
#             break
#     print(result)


# mat([[1,2,3],[4,2,1],[2,1,3]])



def mat(a: list):
    if not a or not all(isinstance(row, list) and row for row in a):
        print(False)
        return
    
    res = {}
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] in res:
                res[a[i][j]] += 1
            else:
                res[a[i][j]] = 1
    
    # Check if all occurrences are equal
    result = len(set(res.values())) == 1
    print(result)

# Test the function
mat([[1, 2, 3], [4, 2, 1], [2, 1, 3]])  # Should output False
