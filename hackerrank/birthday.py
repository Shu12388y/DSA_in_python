def birthday(arr):
    count = 0
    for i in range(0,len(s)-m+1):
        temp_sum = 0
        for j in range(i,i+m):
            temp_sum += s[j]
        if temp_sum == d:
            count += 1
    return count
            

print(birthday([1,2,1,3,2]))    


# m is the size of the square
