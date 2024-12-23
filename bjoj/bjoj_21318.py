import sys
input = sys.stdin.readline

n = int(input())
levels = list(map(int, input().split()))

mistake = [1 if levels[i] > levels[i+1] else 0 for i in range(n-1)]
psum = [0] * n

psum[0] = mistake[0]
for i in range(1, n):
    psum[i] = psum[i-1] + mistake[i-1]
    
q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    x-=1
    y-=1
    
    if x == y:
        print(0)
        continue
    
    answer = psum[y] - psum[x]
        
    print(answer)