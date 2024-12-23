def checkStr(s1:str,s2:str):
    if s1[1:len(s1)-1] ==  s2[1:len(s2)-1] and len(s1)%2 == 0 and len(s2)%2 ==0 and s1[0] == s2[len(s2)-1] and s2[0] == s1[len(s1)-1]:
        print(True) 


# checkStr("bank","kanb")
# checkStr("banerk","kanerb")
checkStr("ban","nab")

