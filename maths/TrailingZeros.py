def zeros(n):
    temp=1
    for i in range(2,n+1):
        temp=temp*i
    res=0
   
    for i in range(1,len(str(temp))):
        if(temp%10==0):
            res=res+1
            temp=temp//10
    return res



# def zeros(n):
#     temp=1
#     for i in range(2,n+1):
#         temp=temp*i
#     res=0
#     while(temp%10==0):
#         res+=1
#         temp=temp//10
#     return res
def main():
    val=int(input("enter the number "))
    print(zeros(val))


main()
