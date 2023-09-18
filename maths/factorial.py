# write a function that return factorial of givrn input

def fact(n):
    temp=1
    for i in range(1,n+1):
        temp=temp*i
    return temp



def main():
    val=int(input("enter the number "))
    print(fact(val))




main()    