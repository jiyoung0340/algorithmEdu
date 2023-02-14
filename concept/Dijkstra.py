# 다익스트라 알고리즘
# 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해
# 매 단계마다 1차원 테이블의 모든 원소를 확인(순차탐색)한다.
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한값

n, m = map(int, input().split()) # 노드 개수, 간선 개수
start = int(input()) # 시작 노드
graph = [[] for i in range(n + 1)] # 각 노드에 연결되어 있는 노드 정보
visited = [False] * (n + 1) # 방문 체크 목적 리스트
distance = [INF] * (n + 1) # 최단 거리 테이블(무한으로 초기화)

# 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a 노드에서 b로 가는 비용 = c

# 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드의 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]: # 시작 노드에 연결된 각 노드의 거리 갱신
        distance[j[0]] = j[1]
    for i in range(n - 1): # n - 1 : 마지막 노드는 안해도 ok. i : 단계!!
        now = get_smallest_node() # now : 가장 짧은 거리의 노드
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

