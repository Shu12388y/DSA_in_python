#  we have to write a function that check the number is pallindom or not

def valPal(n):
    ld=0
    rev=0
    temp=n
    while temp!=0:
        ld=temp%10
        rev=rev*10+ld
        temp=temp//10

    if n==rev:
        print("The number is pallindrom")
    else:
        print("Not a pallindrom")        


def main():
    val=int(input("Enter a number "))
    valPal(val)


main()