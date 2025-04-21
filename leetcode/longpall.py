def longestPallidrome(s:str):
    first = 0 
    second = len(s)-1
    for i in range(0,len(s)):
        if s[first] == s[second]:
            if s[first:second] == s[first:second:-1]:
                return
        else:
            first+=1
            second-=1
    print(s[first:second])

longestPallidrome('babad')