def gcd(a,b):
    temp=0
    if (a<b):
        temp=a
        while(a%temp==0 and b%temp==0):
            temp=temp-1
        return temp
    else:
        temp=b
        while(a%temp==0 and b%temp==0):
            temp=temp-1
        return temp    

def main():
    val1=int(input("enter the number "))
    val2=int(input("enter the number "))

    print(gcd(val1,val2))


main()      