# In this program we have to calculate the number of digit in a number
# for example: n=5678 , digit=4

# first solution
def countDigit(n):

    temp=len(str(n))
    return temp


# second solution
def countDigit1(n):
    res=0
    while n>0:
        n=n//10
        res=res+1
    return res

def main():
    val=int(input("Enter the number "))
    # print(countDigit(val))
    print(countDigit1(val))



main()    