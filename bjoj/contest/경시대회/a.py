m = int(input())
n = int(input())

fruit = []
for i in range(n):
    fruit.append(int(input()))
    

fruit.sort(reverse=True)
sum = 0
idx = 0
while True:
    if n < m:
        break
    sum += fruit[idx+m-1]*m
    idx += m
    n -= m
    
print(sum)

# 2 5 8 11