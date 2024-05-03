def stringCount(st):
    stringArray=[]
    count = 0
    first=[]
    for i in st:
        stringArray.append(i)
    for i in range(len(stringArray)):
        for j in range(i+1,len(stringArray)-1):
            if(stringArray[i] != stringArray[j]):
                first.append(stringArray[i])
        
        # if(i == i+1):
        #     stringArray.remove(i)
        #     stringArray.remove(i+1)

  
          

    return first



print(stringCount("leetcode"))
