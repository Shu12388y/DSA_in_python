# def checkString(str:str)->int:
#     list1 = 0
#     list2 = 0
#     for i in range(len(str)):
#         if str[i] == "*":
#             list1 += 1
#         if str[i] == "#":
#             list2 += 1
#     if list1 > list2:
#         return 1
#     if list2 > list1:
#         return -1
#     if list1 == list2:
#         return 0


def checkString(str:str)->int:  # T.C. O(n)
    hashed = {"*": 0, "#": 0}  # Initialize the count for '*' and '#' to 0
    for char in str:
        if char == "*":
            hashed["*"] += 1
        elif char == "#":
            hashed["#"] += 1
    if hashed["*"] > hashed["#"]:
        return 1
    if hashed["*"] < hashed["#"]:
        return -1
    if hashed["*"] == hashed["#"]:
        return 0
        


print(checkString("samp*le*##jfiihi*8##jif**"))



# print(checkString("shu*ubh##jk"))    