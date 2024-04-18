def time(year):
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        return "12:09:" + str(year)
    else:
        return "13:09:" + str(year)


print(time(1800))   
# output: 12:09:1800  
print(time(2017))   
#  


print(2017%4)