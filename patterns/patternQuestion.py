def PatternQuestion():
    for i in range(4):
        for j in range(0,i):
            print(i,end="")
        print()    


PatternQuestion()    

# output:
# 1
# 22
# 333



def PatternQuestion2():
    for i in range(6):
        for j in range(0,i):
            print(i,end="")
        print()



PatternQuestion2()  

# ouput:
# 1
# 22
# 333
# 4444
# 55555



def PatternQuestion3():
    for i in range(0,4):
        for j in range(0,i):
            print(chr(i+64),end="")
        print()  

PatternQuestion3()          

# output:
# A
# BB
# CCC



def PatternQuestion4():
    for i  in range(8):
        for j in range(0,i):
            print(chr(i+64),end="")
        print()    


PatternQuestion4()

# output:
# A
# BB
# CCC
# DDDD
# EEEEE
# FFFFFF
# GGGGGGG


def PatternQuestion5():
    for i in range(7):
        for j in range(0,i):
            print(chr(64+i),end="")
        print()    


PatternQuestion5()  
# Output:
# A
# BB
# CCC
# DDDD
# EEEEE
# FFFFFF   