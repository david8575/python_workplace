def josephus(n,k):
    nums = [i+1 for i in range(n)]
    result = []
    idx = 0
    while len(nums) != 0:
        idx = (idx + k - 1) % len(nums)
        result.append(nums.pop(idx))

    return result
