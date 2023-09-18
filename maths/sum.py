# we havw to find the sum of n natural numbers
# define function
def sum(n):
    temp=0
    for i in range(n+1):
        temp=temp+i
    
    return temp 


def main():
    val=int(input("Enter the numer "))
    print(sum(val))


main()    