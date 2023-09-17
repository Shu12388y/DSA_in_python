# write a function that take a input and print sum of n natural number
# time complexity is n
def sum(n):
    temp=0
    for x in range(1,n+1):
        temp=temp+x
    return temp    
# time complexity is 1

def fun1(n):
    sum=(n*(n+1))/2
    return sum


# time complexity is n*n
def fun3(n):
    sum=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum=sum+1
    return sum        




def main():
    n=int(input("Enter the number "))
    print(fun3(n))



main()
