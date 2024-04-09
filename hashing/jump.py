def jump(x1,v1,x2,v2):
    for _ in range(1000):
        x1 = x1 + v1
        x2 = x2 + v2
        if(x1==x2):
            return "Yes"     
    else:
        return "NO"        




# print(jump(0,2,5,3))
# print(jump(0,3,4,2))

     