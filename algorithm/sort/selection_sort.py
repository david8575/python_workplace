def selectionSort(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] >= nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

nums = [5,4,9,7,0,3,4,2,5,7,9,10,2,6,5]
selectionSort(nums)
print(nums)