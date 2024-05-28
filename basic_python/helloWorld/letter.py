# def letter(d:list)->int:
#     hashPresent ={}
#     checkedPresnt={}
#     maxs=0
#     count = 0
#     for i in range(len(d)):
#         hashPresent[d[i]]=True
#     for j in range(len(d)):
#         if d[j]-1 in hashPresent:
#             checkedPresnt[d[j]] = True
#             count += 1
#     # maxs = max(maxs,count)
#     return checkedPresnt





# print(letter([1,2,3,4,5,6]))



# def subArray(d:list)->int:
#     newArray=[]
#     for i in range(len(d)):
#         for j in range(i+1,len(d)):
#             if d[i]