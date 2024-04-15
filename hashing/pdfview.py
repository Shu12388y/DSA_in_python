def pdfView(h,word):
    listWord = []
    val=[]
    listAlpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in word:
        listWord.append(i)
    for i  in range(len(listWord)):
        temp = listAlpha.index(listWord[i])
        val.append(h[temp])
    val.sort()
    return val[len(val)-1]*len(listWord)




print(pdfView([1,3, 1, 3, 1 ,4 ,1 ,3 ,2 ,5 ,5, 5, 5, 5, 5 ,5 ,5, 5, 5, 5, 5, 5, 5 ,5 ,5 ,5],"abc"))    