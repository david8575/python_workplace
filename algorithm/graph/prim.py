"""
<프림 알고리즘(Prim)>
그래프에서 최소 신장 트리(MST)를 구하기 위한 알로리즘
MST는 가중치가 부여된 무방향 그래프에서 모든 노드를 포함하면서 사이클이 없고,
간선의 가중치의 합이 최소가 되는 트리

Prim 알고리즘의 특징:
    1. 시작 노드에서 출발하여 트리를 점진적으로 확장합니다.
    2. 항상 현재까지의 트리와 연결된 간선 중 가장 작은 가중치를 가진 간선을 선택합니다.
    3. 이 과정을 반복하며 MST를 구성합니다.
"""

import heapq
from collections import defaultdict

def prim(graph, start_node):
    # 최소 신장트리를 저장할 리스트
    mst = []
    # 방문한 노드를 기록하는 집합 
    visited = set()
    # 최소 힙 -> (가중치, 현재 노드, 이전 노드)
    min_heap = [(0, start_node, None)]
    # 최소 신장 트리의 총 가중치
    total_cost = 0
    
    # 탐색 시작
    while min_heap:
        # 현재 힙에서 가장 작은 가중치를 가진 간선 추출
        weight, current_node, from_node = heapq.heappop(min_heap)
        
        # 이미 방문한 노드면 무시
        if current_node in visited:
            continue
        
        # 현재 노드를 방문 처리
        visited.add(current_node)
        # MST 가중치에 간선 가중치 추가
        total_cost += weight
        
        # 최소 신장 트리에 간선 추가 (루트 노드는 from_node가 None)
        if from_node is not None:
            mst.append((from_node, current_node, weight))
            
        # 현재 노드와 연결된 간선을 힙에 추가
        for next_node, edge_weight in graph[current_node]:
            if next_node not in visited:
                heapq.heappush(min_heap, (edge_weight, next_node, current_node))
                
    return mst, total_cost