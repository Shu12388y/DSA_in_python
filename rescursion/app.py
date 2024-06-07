# function call itself again and again




# print something n times
def recursive(n):
    count = 0
    if count == n:
        return
    print(count)
    count += 1
    recursive(n)


# recursive(10)




# print name n times


def printName(i,n):
    if i>n:return
    print('shubham')
    printName(i+1,n)


# printName(1,4)



# second way

def printname(n:int) -> str:
    if n==0:return
    print('shubham')
    printname(n-1)

# printname(4)    




# print 1 to N


def printN(i:int,n:int)->int:
    if i==n+1:return
    print(i)
    printN(i+1,n)


# printN(0,4)   


# print N to 1


def nPrint(n:int) -> int:
    if n==0:return
    print(n)
    nPrint(n-1)


nPrint(10)
    