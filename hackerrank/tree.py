def tree(n):
    ans =1
    for i in range(1,n+1):
        if i%2 != 0:
            ans =  ans*2
        else:
            ans = ans+1
    return ans            


for i in range(1,6):
    print(tree(i))