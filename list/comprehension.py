# creating a list
l1 = [x for x in range(10)]


print(l1)
# output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# make a list with even number 

l2 = [x for x in range(11) if x%2==0]

print(l2)

# output: [0, 2, 4, 6, 8, 10]


# make a list that separate the even and odd terms
def seprator(l):
    even = [ x for x in l if x%2==0]
    odd = [x for x in l if x%2!=0]
    return even,odd

print(seprator([1,2,3,4,0,5,6,0,7]))
# output: ([2, 4, 0, 6, 0], [1, 3, 5, 7]) 