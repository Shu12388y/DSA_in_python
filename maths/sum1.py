# other way to find the sum of n natural number

def sum(n):
    sum=(n*(n+1))/2
    return sum 


def main():
    val=int(input("enter the number "))
    print(int(sum(val)))


main()    