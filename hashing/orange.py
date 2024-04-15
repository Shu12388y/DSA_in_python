def orangeandapple(apples,orange,s,t,a,b):
    apples_count = 1
    orange_count = 1
    for i in range(len(apples)):
        apples[i] = apples[i]+a
        if apples[i] >=s and apples[i]<=t:
            apples_count = apples_count +1 
    for i in range(len(orange)):
        orange[i] = orange[i]+b
        if orange[i] >=s and orange[i] <= t:
            orange_count = orange_count +1       
    print(apples_count)
    print(orange_count)



orangeandapple([2,3,-4],[3,-2,-4],7,10,4,12)