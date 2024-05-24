def hashString(s: str) -> int:
    map = {}
    index = 0 
    for i in range(len(s)):
        if s[i] in map:
            map[s[i]] += 1
        else:
            map[s[i]] = 1
        
        while index < len(s) and map[s[index]] > 1:
            index += 1
        
        if index == len(s):
            return -1
    
    return index
      



print(hashString("leetcode"))