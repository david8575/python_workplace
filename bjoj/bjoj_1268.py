n = int(input())

table = []
same = [0] * n

for i in range(n):
    table.append(list(map(int, input().split())))
    same[i] = [0] * n

for i in range(5):
    for j in range(n):
        for k in range(j+1,n):
            if table[j][i] == table[k][i]:
                same[k][j] = 1
                same[j][k] = 1
            
cnt = []
for s in same:
    cnt.append(s.count(1))
    
print(cnt.index(max(cnt))+1)