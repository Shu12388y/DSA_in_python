def findBalloon(s:str):
    f = {
        'b':0,
        'a':0,
        'l':0,
        'o':0,
        'n':0
    }

    for i in range(len(s)):
        if s[i] == 'b':
            f['b'] += 1
        if s[i] == 'a':
            f['a'] += 1
        if s[i] == 'l':
            f['l'] += 1
        if s[i] == 'o':
            f['o'] += 1
        if s[i] == 'n':
            f['n'] += 1
    
    if f['b']%2 != 0  and f['a'] % 2 != 0 and f['l'] %2 == 0 and f['o'] % 2 == 0 and f['n']%2 != 0:
        return True
    else:
        return False



print(findBalloon('agirlissusingaballoon'))