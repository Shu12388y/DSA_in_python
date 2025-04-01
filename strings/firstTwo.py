# help me -> HElp ME

def convertFirstTwo(s:str):
    count = 1
    res = ""
    for i in s:
        if(i==" "):
            count = 0
        if(count <=2):
            res+=i.upper()
            count+=1
        else:
            res+=i
    print(res)

    

convertFirstTwo("help me")