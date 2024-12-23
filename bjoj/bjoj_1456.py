import math

n, m = map(int, input().split())
a = [0] * (10000001)

for i in range(2, len(a)):
    a[i] = i
    
for i in  range(2, int(math.sqrt(len(a))+1)):
    if a[i] == 0:
        continue
    for j in range(i+1, len(a)+1):
        a[j] = 0
        
count = 0