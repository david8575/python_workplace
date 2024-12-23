"""
DFS(Depth-First Search) 깊이 우선 탐색
그래프의 한 정점에서 시작하여 가능한 깊이까지 탐색한 후,
더이상 탐색할 곳이 없으면 이전 단계로 되돌아가는 방식

1. 특징
    1) 먼저 한 경로로 끝까지 이동 -> 다른 경로를 탐색
    2) 사용 사례
        - 경로 탐색
        - 사이클 검사
        - 연결 요소 찾기
    3) 시간 복잡도
        - 인접 리스트: O(V+E)
        - 인접 행렬: O(V^2)
2. 구현
    1) 재귀 방식: 함수 호출 스택을 활용하여 간결하게 구현
    2) 스택 방식: 명시적으로 스택을 사용하여 반복문으로 구현
    3) 비교
        - 재귀 방식은 간결하지만, 스택 오버플로우 위험이 있음
        - 스택 방식은 명시적인 스택을 사용해 더 큰 그래프에서도 안전하게 동작
"""

# 재귀 방식
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(neighbor, visited)
            
# 스택 방식
def dfs_stack(graph, start):
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                stack.extend(reversed(list(graph[node].keys())))