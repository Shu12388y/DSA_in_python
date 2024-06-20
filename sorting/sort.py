def insertingSort(n:list)->list:
    minNums = 0 
    for i in range((len(n))):
        for j in range(i+1,len(n)):
            if n[i] > n[j]:            # 2 > 4 no => 2 > 1 yes  minNums = 2  n[i] = 1 n[j] = 2 ==> [1,4,2,5] 
                minNums = n[i]
                n[i] = n[j]
                n[j] = minNums
    return n

 
# print(insertingSort([13,46,24,52,20,9]))



def bubbleSort(n:list)->list:
    temp = 0
    for _ in range(len(n)):
        for j in range(len(n)-1):
            if n[j] > n[j+1]:
                temp = n[j]
                n[j] = n[j+1]
                n[j+1] = temp
    return n            
print(bubbleSort([1,10,8,7]))



# optimize bubble sort

def optimizeBubbleSort(n:list):
    for i in range(len(n)):
        swapped = False
        for j in range(len(n)-i-1):
            if n[j] > n[j+1]:
                n[j],n[j+1] = n[j+1],n[j]
                swapped = True
        if swapped == False:
            return
        return n
    

print()    

                
