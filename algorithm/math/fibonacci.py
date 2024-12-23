# 피보나치 함수 fibonacci

# 피보나치 함수 1 : 단순 반복
def fibonacci_1(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_1(num-1) + fibonacci_1(num-2)
    
# 피보나치 함수 2 : 리스트에 저장
def fibonacci_2(num):
    fibonacci_list = [0,1]
    if num <= 1:
        return fibonacci_list[num]
    else:
        for i in range(2, num+1):
            fibonacci_list.append(fibonacci_list[i-1]+fibonacci_list[i-2])
        return fibonacci_list[num]
    
# 피보나치 함수 3 : 0과 1이 몇 번 호출 되었는 지
def fibonacci_count(n):
    cnt = [(1,0), (0,1)] + [(0,0)] * (n-1)
    for i in range(2,n+1):
        cnt[i] = (cnt[i-1][0] + cnt[i-2][0], cnt[i-1][1] + cnt[i-2][1])
    return cnt[n]