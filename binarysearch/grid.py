def countNegatives(grid) -> int:
    countNeg = 0
    for i  in range(len(grid)):
        for j in grid[i]:
            if j < 0:
                countNeg+=1
    return countNeg

print(countNegatives([[5,1,0],[-5,-5,-5]]))