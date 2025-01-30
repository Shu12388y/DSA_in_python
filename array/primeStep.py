def checkPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def countPrime(a: list):
    count = 0
    
    for i in range(len(a)):
        if not checkPrime(a[i]):  
            temp = a[i]
            while True:
                temp += 1  
                count += 1  # Increment count since we are changing the number
                if checkPrime(temp):  # Stop when we find a prime
                    break

    print(count)

# Test the function
countPrime([9, 5, 5, 6])
