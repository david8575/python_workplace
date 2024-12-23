import sys
input = sys.stdin.readline
# 1차원 합 배열
def preFix(nums):
    preFixSum = [0]
    for num in nums:
        preFixSum.append(preFixSum[-1] + num)
    return preFixSum
# 1차원 구간 합
# preFixSum[e] - preFixSum[s-1] -> 인덱스 e부터 s까지의 합

# 2차원 합 배열
def preFix2(nums):
    preFixSum = [[0] * (len(nums[0])+1) for _ in range(len(nums[0])+1)]
    for i in range(1, len(nums[0])+1):
        for j in range(1, len(nums[0])+1):
            preFixSum[i][j] = preFixSum[i][j-1] + preFixSum[i-1][j] - preFixSum[i-1][j-1] + nums[i][j]
    return preFixSum
# 2차원 구간 합
# preFixSum[x2][y2] - preFixSum[x1-1][y2] - preFixSum[x2][y1-1] + preFixSum[x1-1][y1-1] -> (x2, y2)에서 (x1, y1)까지 합