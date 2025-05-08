def FindPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)

mylist = [1, 2, 3, 4, 5, 1, 2, 3, 8, 9, 7]
FindPairs(mylist, 8)