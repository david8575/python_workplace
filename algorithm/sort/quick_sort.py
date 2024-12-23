def quickSort(nums):
    if len(nums) <=1 :
        return nums
    pivot = nums[len(nums) // 2]
    left = [num for num in nums if num < pivot]
    right = [num for num in nums if num > pivot]
    mid = [num for num in nums if num == pivot]

    return quickSort(left) + mid + quickSort(right)

list1 = list(map(int, input().split()))
print(list1)
list1 = quickSort(list1)
print(list1)