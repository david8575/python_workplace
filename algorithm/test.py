from datastruct.graph import Graph
from graph.dfs import dfs_recursive, dfs_stack

# 그래프 생성 및 초기화
g = Graph()
g.add_node('A')
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
g.add_edge('E', 'F')
g.add_edge('D', 'F')

# 그래프 출력
print("Graph:")
for node, edges in g.get_graph().items():
    print(f"{node}: {edges}")

# DFS 테스트 (재귀 방식)
print("\nDFS (Recursive):")
g.dfs_recursive('A')

# DFS 테스트 (스택 기반)
print("\n\nDFS (Stack):")
g.dfs_stack('A')