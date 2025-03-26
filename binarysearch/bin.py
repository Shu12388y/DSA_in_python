def bin(start,end,n):
    first  = start
    last =  end
    while(first + 1 < last):
        mid = int((first+last)/2)
        if(mid == n):
            first =  mid 
        else:
            last = mid
    print(first,last)

bin(1,10,7)