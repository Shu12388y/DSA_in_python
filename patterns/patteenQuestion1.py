def PatternQuestion1():
    for i in range(0,5):
        for j in range(0,i):
            print(chr(j+64+i),end="")
        print()    

PatternQuestion1()

# output:
# A
# BC
# CDE
# DEFG



def PatternQuestion2():
    for i in range(0,6):
        for j in range(0,i):
            print(chr(64+i+j),end="")
        print()    


PatternQuestion2()        
# output:
# A
# BC
# CDE
# DEFG
# EFGHI

def PatternQuestion3():
    for i in range(0,5):
        for j in range(0,i):
            print(chr(69-i+j),end="")
        print()    

PatternQuestion3()  
# Output:
# D
# CD
# BCD
# ABCD   