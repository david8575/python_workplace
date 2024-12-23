m, n = map(int, input().split())

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

idx_1 = 0
idx_2 = 0
while (idx_1 < m and idx_2 < n):
    a = list_a[idx_1]
    b = list_b[idx_2]
    if (a <= b):
        print(a, end=" ")
        idx_1+=1
    else:
        print(b, end=" ")
        idx_2+=1

for i in range(idx_1, m):
    print(list_a[i], end=" ")
for i in range(idx_2, n):
    print(list_b[i], end=" ")