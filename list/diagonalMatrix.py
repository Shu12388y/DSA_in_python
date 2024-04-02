def diagonalMatrix(arr):
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)):
        for j in range(0,4):
            if(i==j):
                print(arr[i][j])
    for i in range(len(arr)):
        for j in range(0,4):
            if i+j == 2:
                print(arr[i][j])


print(diagonalMatrix([[1,2,3],[2,3,4],[5,6,7]]))
                


arrNew = [[1,3,2],[3,4,5],[5,6,7]]
print(len(arrNew))
