def main(r,f,arr):
    if len(arr) == 0:
        return -1
    rate = r*f
    sum = 0
    for i in arr:
        if sum >rate:
            return sum-rate 
        sum = sum+i
    else:
        return 0







if __name__ == "__main__":
    print(main(5, 3, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))