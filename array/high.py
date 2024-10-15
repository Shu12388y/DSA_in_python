def high(gain:list)->int:
    gainList = [0]*(len(gain))
    gainList[0] = gain[0]
    for i in range(1,len(gain)):
        gainList[i] = gainList[i-1] + gain[i]
    print(max(gainList))

high([-5,1,5,0,-7])