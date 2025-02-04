def encrypt(i: int):
    encryptNumber = str(i)
    temp = ""
    for i in range(len(encryptNumber) - 1):
        if (int(encryptNumber[i]) + int(encryptNumber[i + 1])) > 9:
            t1 = str(int(encryptNumber[i]))
            t2 = str(int(encryptNumber[i + 1]))
            temp += str(str(t1[:-1]) + str(t2[:-1]))
        temp += str(int(encryptNumber[i]) + int(encryptNumber[i + 1]))
    print(temp)


encrypt(4567)
