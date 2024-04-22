def threshold(k,arr):
    count = 0
    for i in range(len(arr)):
        if (arr[i]<=0):
            count = count+1
    print(count)            
    if count>=k:
        print("NO")
    else:
        print("YES")            



threshold(3,[-2,-1,0,1,2])    
threshold(3,[-1, -3, 4, 2])    
threshold(2,[0, -1, 2, 1])