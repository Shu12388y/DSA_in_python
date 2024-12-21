
# logical operator
a,b = 5,3
print(a and b)
print(a or b)
print(not a)
print(not b)


# bitwise operator
print(a | b)
print( a & b)
print( a ^ b)

# get binary equvialent
print(bin(2))


# shift
print( a << b) # right shift
print( a >> b) # left shift


# identify opertor
g = [10,15,20]
p = [10,15,20]
print(g is p)
print (g is not p)


# Membership operator
l = [1,2,3,4,6,56]
print( 9 in l)
print (10 in l)
print(99 not in l)



# escape a particular iteration
for i in range(0,10):
    if i == 6:
        continue
    print(i)

# break a particulat iteration
for i in range(0,10):
    if i == 6:
        break
    print(i)



# pass 
test = 'GURU'
for i in test:
    if i == 'U':
        print('Pass is executed')
        pass
    print(i)


# list
# 1. It is mutable
# 2. It can handle any data types
# 3. It is Indexable 
# 4. It is sortable an allow  duplicates


lst = [1,2,3,5,0,6]

print([x for x in dir(lst) if '__' not in x])  # give out the  methods of the list




lst.append([12,3,4,'CSE','IT','ECE'])
# list slicing
print(lst)


# print cse and it
# [3:5] ==> 3,4
print(lst[6][3:5])

# reverse [:-8:-1]  or [::-1]





