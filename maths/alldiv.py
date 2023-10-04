def alldiv(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)


def main():
    val=int(input("enter the number "))
    alldiv(val)

main()                
    