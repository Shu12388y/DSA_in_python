# maths in coding
import math


def functionMaths1(n):
    # get the digit of number
    while n>=1:
        last=n%10
        print(int(last))  
        n = n//10

    

# count the number of digits
# T.C. O(ln10(n))
def countDigit(n):
    count = 0
    while n>1:
        count +=1
        n = n/10
    return count         

# solution 2 (oprtimis)

def countDigits(n):
    cnt = int(math.log10(n) + 1)
    return cnt




#  Reverse the number 
def reverseNums(n):
    reversen = 0
    last = 0 
    if n>0:
        while n>1:
            last = n%10
            n = n/10
            reversen = (reversen*10)+int(last)
        return reversen 
    else:
        n = abs(n)
        while n>0:
            last = n%10
            n = n/10
            reversen = (reversen*10)+int(last)
        return -int(reversen) 
    



# time complexity is O(d) depend on the nums of digits

def pallidrome(n):
    compStr = n
    res = 0
    res= int(str(n)[::-1])
    if res == compStr:
        return "pallidrome"
    else:
        return "No a pallidrome"


def pallidrome1(n:int) -> bool:
    return str(n) ==  str(n)[::-1]






def main():
    # functionMaths1(1234)
    # print(countDigit(12345))
    # print(countDigits(12345))
    # print(reverseNums(10))
    # print(pallidrome(4553))
    print(pallidrome1(122))



main()    