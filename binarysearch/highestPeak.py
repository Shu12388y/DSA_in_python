# find the highest mountain peak
# A = [2,4,5,9,8,7];



def highestPeak(a:list):
    left = 0
    right = len(a)
    while  left + 1 < right:
        mid = (left + right) // 2
        if(a[mid] >  a[mid-1]):
            left = mid
        else:
            right =  mid
    print(a[mid-1])

highestPeak([2,4,5,9,8,7])