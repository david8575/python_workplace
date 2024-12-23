# 팩토리얼 factorial

# 단순 반복
def factorial_1(num):
    ans = 1 
    for i in range(1, num+1):
        ans *= i
    return ans

# 재귀함수 이용
def factorial_2(num):
    if num == 1:
        return 1
    else:
        return num * factorial_2(num-1)