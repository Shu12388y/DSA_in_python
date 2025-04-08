import math


def findPerfectSqrt(x:int):
    res = math.floor(math.sqrt(x))
    if(res * res == x):
        return True
    else:
        return False