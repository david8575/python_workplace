num = int(input())

ans = 0
cnt = 0
while True:
    if num < 10:
        num = num * 10
    sum_of_digits = (num // 10) + (num % 10)
    num = ((num % 10) * 10) + (sum_of_digits % 10)
    cnt += 1
    if num == ans:
        break

    

print(f"{cnt}")