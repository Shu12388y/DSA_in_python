def bill(bil,k,b):
    bil[k] = 0
    total = 0
    for i  in range(len(bil)):
        total += bil[i]
    if total/2 != b:
        return int(b-(total/2))
    else:
        return "Bon Appetit"      


print(bill([3,10,2,9],1,7))