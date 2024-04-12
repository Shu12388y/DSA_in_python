def alphabet():
    for i in range(0,5):
        for j in range(0,i):
            print(chr(65+j),end="")
        print()    



alphabet()


# output:
# A
# BB
# CCC
# DDDD


# output: 
# A
# AB
# ABC
# ABCD