from collections import deque
from itertools import combinations

n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

cells = [(i,j) for i in range(n)for j in range(m) if map[i][j] == 0]

answer = 0
for combination in combinations(cells, 3):
    for row, col in combination:
        map[row][col] = 1
        
    visit = [[False] * m for _ in range(n)]
    queue = deque()
    
    for i in range(n):
        for j in range(m):
            if map[i][j] == 2:
                queue.append((i, j))
                visit[i][j] = True
                
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    while len(queue) != 0:
        r, c = queue.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if nr < 0 or n <= nr or nc < 0 or m <= nc:
                continue
            if map[nr][nc] == 1:
                continue
            if not visit[nr][nc]:
                queue.append((nr,nc))
                visit[nr][nc] = True
    
    safe = 0
    for i in range(n):
        for j in range(m):
            if map[i][j] == 0 and not visit[i][j]:
                safe +=1
    answer = max(answer, safe)
        
    for row, col in combination:
        map[row][col] = 0
        
print(answer)