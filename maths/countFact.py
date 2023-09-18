# write a function that return factorial of given input
# also found the sum of digit of the factorial
def fact(n):
    temp=1
    count=0
    for i in range(1,n+1):
        temp=temp*i
    

    return temp


def count(m):
    n=fact(m)
    res=0
    while n>0:
        n=n//10
        res=res+1
    return res    




def main():
    val=int(input("enter the number "))
    print(count(val))




main()    