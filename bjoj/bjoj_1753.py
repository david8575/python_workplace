import heapq

v, e = map(int, input().split())
start = int(input())

graph = [[] for _ in range(v+1)]
for i in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((w,v))

for i in range(1, v+1):
    if graph[i]:
        for weight, end in graph[i]:
            print(f'{i} --{weight}-> {end}')
            
print(graph)