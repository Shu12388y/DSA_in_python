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
    for i in range(0,6):
        for j in range(1,i):
            print(j,end="")
        print()    


def pattern4():
    for i in range(0,5):
        for j in range(0,5-i):
            print("*",end="")
        print()            


def pattern5():
    for i in range(0,6):
        for j in range(1,6-i):
            print(j,end="")
        print()  



def pattern6():
    for i in range(0,5):
        for j in range(0,5-i+1):
            print(" ",end="")
        for j in range(0,2*i+1):
            print("*",end="")
        for j in range(0,5-i+1):
            print(" ",end="")        
        print()            

def pattern7():
    for i in range(0,5):
        for j in range(0,i):
            print(" ",end="")
        for j in range(0,9-(2*i)):
            print("*",end="")
        for j in range(0,i):
            print(" ",end="")
        print()            

def pattern8():
    pattern6()
    pattern7()



def pattern9():
    pattern2()
    pattern4()



def pattern10():
    start =1
    for i in range(1,5):
        if i%2 == 0:
            start = 1
        else:
            start=0     
        for j in range(0,i):
            print(start,end="")
            start = 1-start
        print()    




def pattern11():
    for i in range(0,5):
        for j in range(0,5-i-1):
            print(" ",end="")
        for j in range(0,i+1):
            print("*",end="")
        print()    









def main():
    # pattern1()
    # pattern2()
    # pattern3()
    # pattern4()
    # pattern5()
    # pattern6()
    # pattern7()
    # pattern8()
    # pattern9()
    # pattern10()
    pattern11()


main()
