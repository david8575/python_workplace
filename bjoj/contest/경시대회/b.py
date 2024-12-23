n = int(input())

count = 0

for i in range(1,n):
    for j in range(1,n):
        a = j
        b = j + i
        c = j + (i*2)
        
        if c <= n:
            count+=1

print(count)