def hashCount(n:list):
    hashArray = [0]*(max(n)+1)
    for i in range(len(n)):
        hashArray[n[i]] += 1
    for i in range(len(hashArray)):
        print({i:hashArray[i]})


hashCount([1,3,4,5,5,6,9])