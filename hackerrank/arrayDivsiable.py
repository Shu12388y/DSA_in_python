def getTotalX(a, b):
    # Write your code here
    max_a = max(a)
    max_b = max(b)
    count = 0
    for i in range(max_a,max_b+1):
        good = True
        for k in a:
            if i%k != 0:
                good =False
        for p in b:
            if p%i != 0:
                good = False
        if (good):
            count += 1
    return count                
    