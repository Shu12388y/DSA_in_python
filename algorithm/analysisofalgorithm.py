# write a function that take a input and print sum of n natural number
def sum():
    number=int(input("enter your number "))
    temp=0
    for x in range(number+1):
        temp=temp+x
    return temp    


def main():
    print(sum())



main()
