def main(l: list) -> int:
    if len(l) == 1:
        return l[0]
    
    # Dictionary to count occurrences of each element
    count_dict = {}
    for i in l:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    
    # Find the element with the highest count
    most_frequent = max(count_dict, key=count_dict.get)
    
    return most_frequent

if __name__ == "__main__":
    print(main([1, 2, 2]))
