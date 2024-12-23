# def prefix(a:list):
#     sortedPrefix = sorted(a)
#     temp = sortedPrefix[0]
#     res = ''
#     # print(temp)
#     # time complexity O(n**2)
#     for i in range(1,len(sortedPrefix)):
#         for j in sortedPrefix[i]:
#             if j  in temp:
#                 res += j
#     # print(set(res))
#     print(res)
        


# # prefix(['flower','flow','floss'])
# prefix(['hello','hellowe','hellpwo'])



def prefix(a: list):
    if not a:
        print("")  # Return an empty string for an empty input list
        return

    # Sort the list of strings
    sortedPrefix = sorted(a)
    first = sortedPrefix[0]
    last = sortedPrefix[-1]
    # print(first)
    # print(last)

    common_prefix = ""
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            common_prefix += first[i]
        else:
            break

    print(common_prefix)


# Test cases
prefix(['flower', 'flow', 'floss'])  # Output: "flo"
prefix(['hello', 'hellowe', 'hellpwo'])  # Output: "hell"
