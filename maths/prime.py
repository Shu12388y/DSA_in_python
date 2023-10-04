def prime(a):
    if a>0:
        for i in range(2,a):
            if(a%i==0 and a%1==0):
                return "no"
            else:
                return "yes"
        
    else:
        print("number should be positive")  
        
        
def main():
    num=int(input("enter the number"))
    print(prime(num))        


main()    