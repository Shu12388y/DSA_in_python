def pattern1():
    for i in range(0,4):
        for j in range(0,4):
            print("*",end="")
        print()    



def pattern2():
    for i in range(0,5):
        for j in range(0,i):
            print("*",end="")
        print()    


def pattern3():
    for i in range(1,5):
        for j in range(1,i):
            print(i,end="")
        print()    



def main():
    # pattern1()
    # pattern2()
    pattern3()


main()
