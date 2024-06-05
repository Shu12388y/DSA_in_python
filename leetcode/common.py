def common(strings:list[str])->int:
    str0 = list(set(strings[0]))
    str1 = list(set(strings[1]))
    str2 = list(set(strings[2]))
    res = []
    for i in range(len(str0)):
        if str0[i] == str1[i] or str0[i] == str2[i]:
            res.append(str0[i])
    return res



print(common(["bella","label","roller"]))