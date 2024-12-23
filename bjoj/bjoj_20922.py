n, k = map(int, input().split())
nums = list(map(int, input().split()))

count = [0] * 10001
start = 0
end = 0
count[nums[start]] += 1

max_len = 0
good = True

while True:
    if good:
        max_len = max(max_len, end-start+1)
        
        if end == n-1:
            break
        
        end += 1
        count[nums[end]] += 1
        if count[nums[end]] == k + 1:
            good = False
    
    else:
        start += 1
        count[nums[start -1]] -= 1
        if (count[nums[start - 1]] == k):
            good = True
    
print(max_len)