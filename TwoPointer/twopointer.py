def SubarrayCounter(arr:list,k:int):
    count = 0 
    for i in range(len(arr)):
        sum = 0 
        for j in range(i,len(arr)):
            sum = sum + arr[j]
            if sum <= k:
                count += 1    
    return count






def main():
    print(SubarrayCounter([2,1,1,5,8],4))




if __name__ == "__main__":
    main()