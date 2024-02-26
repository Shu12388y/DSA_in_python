# linear search

def search(l,number):
    for i in range(0,len(l)-1):
        if l[i] == number:
            return 1
        else:
            return -1



def main():
    f = search([1,2,4,3,5],2)
    if f==1:
        print("1")
    else:
        print("-1")


main()