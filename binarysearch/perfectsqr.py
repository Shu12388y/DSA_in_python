import math


def findPerfectSqrt(x:int):
    res = math.floor(math.sqrt(x))
    if(res * res == x):
        return True
    else:
        return False
    

def findPerfect(x:int):
    x **= 0.5
    num_pref = x//1
    return x == num_pref
    
