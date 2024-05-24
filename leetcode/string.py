def string(s:str) -> int:
    map = {}
    for char in s:
        if char in map:
            map[char] += 1
        else:
            map[char] = 1  

    for i in range(len(s)):
        if map[s[i]] == 1:
            return i

    return -1        
    # for i in range(len(s)):
    #     if s[i] in map:
    #         map[s[i]] +=1
    #     else:
    #         map[s[i]] = 1
        

print(string("aabb"))    