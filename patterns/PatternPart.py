def patterPart():
    for i in range(0,5):
        for j in range (0,5):
            if (j==i):
                print()
            else:
                print("*",end="")
        print()


patterPart()                    