def time(year):
    if year == 1918:
        return '26.09.'+str(year)
    elif year<1918:
        if year%4 ==0:
            return '12.09.'+str(year)
        else:
            return '13.09.'+str(year)
    else:
        if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            return "12:09:" + str(year)
        else:
            return "13:09:" + str(year)


print(time(1800))   
# output: 12:09:1800  
print(time(2017))   
