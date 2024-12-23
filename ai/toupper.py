def toUpper(s: str):
    ref = {
        'a': 'A',
        'b': 'B',
        'c': 'C'
    }
    res = ""
    for char in s:  
        if char in ref:  
            res += ref[char]  
        else:
            res += char  
    print(res)

toUpper('cba')  # Output: "ABC"
