
# [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# [1,2,3,4,5,8,9,12,13,14,15,16]

def matrixBoundary(a:list):
    for i  in range(len(a)):
        if i == 0 or i == 3:
            for j in range(0,len(a)):
                print(a[i][j])
        if i == 1 and j ==  0  or i == 2 and (j == 0 or j== 3):
            for j in range(len(a)):
                print(a[i][j])


matrixBoundary([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])


# 

# ux8@8eDmK7cwLuL