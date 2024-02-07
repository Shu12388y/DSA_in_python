# average of list

def average(lists):
    sum=0
    for i in range(len(lists)):
        sum = sum+ lists[i]
    return sum/len(lists)    


print(average([1 ,2 ,3 ,4 ]))

# output:  2.5



def newAverage(lists):
    return sum(lists)/len(lists)


print(newAverage([1,2,3,4]))    

# output 2.5