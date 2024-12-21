def binaryConverter(n:int):
    res = ""
    while n != 0:
        res = res + str(n % 2)
        n = int(n / 2)
    print(res[::-1])   




binaryConverter(8)
