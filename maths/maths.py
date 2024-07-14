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


def armstrong(n):
    original = n
    last = 0
    res = 0 
    while n > 0:
        last = n%10                   # 3                     5                  1
        res = res + last ** 3         # res = 0 + 27          res = 27 + 125     res = 27+125+1
        n = n // 10                    # n = 153/10  ==> 15    n = 1              n = 0     
    return res==original 




def gcf(n,m):
    factors_n = []
    factors_m = []

    # Find factors of n
    for i in range(1, n + 1):
        if n % i == 0:
            factors_n.append(i)

    # Find factors of m
    for i in range(1, m + 1):
        if m % i == 0:
            factors_m.append(i)

    # Print factors for debugging purposes (optional)
    print("Factors of", n, ":", factors_n)
    print("Factors of", m, ":", factors_m)

    # Find common factors
    common_factors = [factor for factor in factors_n if factor in factors_m]

    # Return the greatest common factor
    return max(common_factors) if common_factors else None



def commonDivisor(n):
    res = []
    for i in range(1,n+1):
        if n%i ==0:
            res.append(i)
    return res            


def prime(n):
    count = 0 
    for i in range(1,n+1):
        if n%i == 0:
            count += 1
    if count>2:
        return "Not Prime"
    else:
        return "Prime"             





def main():
    # functionMaths1(1234)
    # print(countDigit(12345))
    # print(countDigits(12345))
    # print(reverseNums(10))
    # print(pallidrome(4553))
    # print(pallidrome1(122))
    # print(armstrong(153))
    # print(gcf(9,12))
    # print(commonDivisor(36))
    print(prime(4))



main()    