from collections import deque

n = int(input())

nums = [i+1 for i in range(n)]
nums = deque(nums)
for i in range(n-1):
    nums.popleft()
    nums.append(nums.popleft())
    
print(nums[0])