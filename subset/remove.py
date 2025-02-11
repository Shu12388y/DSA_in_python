import re 

def remove(s:str,r:str):
    
    ans = re.findall(r,s)
    print(ans)


remove('daabcbaabcbc','abc')