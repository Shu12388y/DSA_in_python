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
    while n>1:
        last = n%10
        n = n/10
        reversen = (reversen*10)+int(last)
    return reversen    
















def main():
    # functionMaths1(1234)
    # print(countDigit(12345))
    # print(countDigits(12345))
    print(reverseNums(12345))



main()    