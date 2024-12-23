"""
Graph
정점(Vrtex)과 간선(Edge)으로 이루어진 자료구조
네트워크, 지도, 웹페이지 연결 등에 활용
1. 그래프의 표현
    1) 인접리스트(Adjacency List)
        - 각 정점에 연결된 다른 정점들을 리스트로 저장
        - 공간 효율적이며, 연결된 정점을 찾는 데 적합
    2) 인접행렬(Adjacency Matrix)
        - 정점간의 연결 여부를 행렬로 저장
        - 정점의 개수가 적을 때비효율적이나, 두 정점간 연결 여부를 빠르게 확인할 수 있음
"""

class Graph:
    def __init__(self):
        # 노드와 간선을 저장할 딕셔너리
        self.graph = {}
        
    def add_node(self, node):
        # 노드를 그래프에 추가
        if node not in self.graph:
            self.graph[node] = {}
            
    def add_edge(self, from_node, to_node, weight):
        # 방향성 간선 추가
        if from_node not in self.graph:
            self.add_node(from_node)
        if to_node not in self.graph:
            self.add_node(to_node)
        self.graph[from_node][to_node] = weight
    
    def add_undirected_edge(self, node1, node2, weight):
        # 무방향 간선 추가
        self.add_edge(node1, node2, weight)
        self.add_edge(node2, node1, weight)

    def display(self):
        # 그래프 출력
        for node, edges in self.graph.items():
            print(f"{node}: {edges}")

    def get_graph(self):
        # 그래프 반환
        return self.graph