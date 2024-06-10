def charhah(s:str,k:str):
    count = 0
    for i in s:
        if i == k:
            count += 1
    return count



# print(charhah("shubham","m"))



def charHash(s:str):
    hashStr=[0]*26
    aplhabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in s:
        for j in range(len(aplhabet)):
            if i == aplhabet[j]:
                hashStr[j] += 1
    return hashStr             


# print(charHash("shubhamz"))





def charHashed(s:str)->list:
    hashStr = [0]*26
    temp = 0 
    for i in s:
        temp = ord(i) - ord('a')
        hashStr[temp] += 1
    return hashStr


# print(charHashed("shubham"))

 

def hashMap(n:list)->dict:
    maps={}
    for i in range(len(n)):
        if n[i] in maps:
            maps[n[i]] += 1
        else:
            maps[n[i]] = 1
    return maps


print(hashMap([1,2,2,3,4,5,6]))