def findfirst(m:int,n:int,l:list):
    ld = sorted(l)
    if(-n in ld):        
        for i in range(len(ld)):
            if ld[i] + 1 != ld[i+1]:
                return ld[i]+1
    else:
        return 0   

print(findfirst(7,5,[-1 ,4 ,-5 ,3 ,-2 ,-3, 4]))

