def freqArray(l:list):
    freq = [0] * (len(l) + 1)
    f = 0
    for i in range(len(l)):
        if l[i] not in freq:
            freq[l[i]] = 1
        else:
            freq[l[i]] += 1
    print(freq.index(max(freq)))
freqArray([1,1,2,3,2,1])