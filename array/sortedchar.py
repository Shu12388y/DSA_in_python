# sorting string

# "axbccy" --> input
# "abccxy" --> output


# burte force
def sortingStr(s:str):
    res =  str(sorted(s))
    print(res)
    print(''.join(res))
print(sortingStr("shubham"))