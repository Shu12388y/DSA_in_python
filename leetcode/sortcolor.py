def sortColor(nums: list):
    countColor = {}

    for i in range(len(nums)):
        if nums[i] == 0:
            if nums[i] not in countColor:
                countColor[nums[i]] = 1
            else:
                countColor[nums[i]] += 1
    for i in range(len(nums)):
        if nums[i] == 1:
            if nums[i] not in countColor:
                countColor[nums[i]] = 1
            else:
                countColor[nums[i]] += 1
    for i in range(len(nums)):
        if nums[i] == 2:
            if nums[i] not in countColor:
                countColor[nums[i]] = 1
            else:
                countColor[nums[i]] += 1
    nums.clear()
    for i in countColor:
        for j in range(countColor[i]):
            nums.append(i)

    print(nums)




sortColor([2,0,2,1,1,0])