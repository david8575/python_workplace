n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()

start = 0
end = 1
count = 0

while(end == len(nums)):
    if nums[start] + nums[end] == x:
        count+=1
        start+=1
        end=0
    elif nums[start] + nums[end] > x:
        break
    else:
        end+=1

print(count)