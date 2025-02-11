def subSet(arr: list, index: int, combination: list, ans: list):
    # Base case
    if index == len(arr):
        ans.append(combination[:]) 
        return

    # Do not pick the current element
    subSet(arr, index + 1, combination, ans)

    # Pick the current element
    combination.append(arr[index])
    subSet(arr, index + 1, combination, ans)

    # Backtrack (remove last element before returning)
    combination.pop()

def helper():
    ans = []  # Local variable to avoid global issues
    nums = [1, 2, 3]
    subSet(nums, 0, [], ans)
    print(ans)

helper()
