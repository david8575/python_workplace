import sys
input = sys.stdin.readline

def quickSort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2]
    left = [num for num in nums if num < pivot]
    mid = [num for num in nums if num == pivot]
    right = [num for num in nums if num > pivot]
    return quickSort(left) + mid + quickSort(right)

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums = quickSort(nums)
print(nums[m-1])