

def check(l:str):
    count = 0
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            count = count + 1

    return count


print(check('RRBGRBG')) 