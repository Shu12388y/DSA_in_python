def findSub(a:list,target:int):
    current_sum = 0
    start = 0
    for i  in range(len(a)):
        current_sum += a[i]

        while current_sum > target:
            current_sum -= a[start]
            start += 1

        if current_sum == target:
            return start+1,i+1    

            

print(findSub([1 ,2 ,3 ,7 ,5],12))