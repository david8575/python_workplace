"""
<다익스트라 알고리즘(Dijkstra Alg)>
단일 시작점 최단 경로 알고리즘
특정 노트에서 다른 모든 노드까지의 최단 거리를 계산
가중치가 음수가 아닌 그래프에서만 동작 가능

1. 초기화
    1) 시작노드에서 각 노드까지의 최단거리를 무한대로 설정
    2) 시작노드의 거리는 0으로 초기화
    3) 우선순위 큐를 생성하여 (거리, 노드)쌍을 관리
2. 반복과정
    1) 우선순위 큐에서 최단 거리 노드를 pop
    2) 해당 노트와 연결된 모든 이웃노드에 대해, 기존 최단거리보다 짧은 경로를 발견하면 업데이트
    3) 업데이트된 노드를 다시 큐에 삽입
3. 종료
    1) 큐가 빌 때까지 반복
    
시간 복잡도: O(ElogV) (E:간선 개수, V: 노드 개수)
"""
import heapq

def dijkstra(graph, start):
    # 시작노드에서 각 노드까지의 최단 거리
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    # 큐가 빌때까지 반복
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # 이미 처리된 노드 무시
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # 더 짧은 경로를 발견한 경우
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances