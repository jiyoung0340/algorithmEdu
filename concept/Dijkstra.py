# 다익스트라 알고리즘
# 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해
# 매 단계마다 1차원 테이블의 모든 원소를 확인(순차탐색)한다.
import sys
from math import dist

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


# Heap
import heapq

# 오름차순 힙 정렬(Heap Sort) - 최소 힙
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])

# 내림차순 힙 정렬(Heap Sort) - 최대 힙
# 별도의 최대힙 라이브러리를 제공하지않음!
# 따라서 최소힙에서 부호를 바꾸어 push/pop해준다.
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])

# 힙을 이용한 다익스트라 알고리즘
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한값

n, m = map(int, input().split()) # 노드 개수, 간선 개수
start = int(input()) # 시작 노드
graph = [[] for i in range(n + 1)] # 각 노드에 연결되어 있는 노드 정보
distance = [INF] * (n + 1) # 최단 거리 테이블(무한으로 초기화)

# 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a 노드에서 b로 가는 비용 = c

def dijkstraHeap(start):
    q = []
    # 시작 노드로 가기 위한 최단경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1] # i[1] = 인접한 노드까지의 거리 값
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

# 플로이드 워셜 알고리즘
INF = int(1e9) # 무한

# 노드의 개수 및 간선의 개수 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기자신에서 자기 자신으로 가는 비용 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
# 각 간선에 대한 정보 입력 및 초기화
for _ in range(m):
    # A -> B 비용 C
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1): # k : 거쳐가는 노드
    for a in range(1, n + 1): # a : 출발 노드
        for b in range(1, n + 1): # b : 도착 노드
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우 무한으로 출력
        if graph[a][b] == INF:
            print("무한", end=" ")
        # 거리 출력
        else:
            print(graph[a][b], end =" ")
    print()

#Q.전보 문제
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한값

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 노드의 개수, 간선의 개수, 시작 노드 입력받기
n, m, start = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블 초기화
distance = [INF] * (n + 1)

# 간선 정보 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    # x번 노드에서 y번 노드로 가는 비용이 z라는 뜻
    graph[x].append((y, z))

dijkstra(start)

count = 0 # 도달 도시 개수
max_distance = 0 # 도달 가능한 도시중, 가장 멀리있는 도시와의 최단거리
for d in distance:
    if d != 1e9:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야하므로 -1
print(count -1, max_distance)

# Q. 미래도시
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 간선 정보 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐갈 노드 x와 최종 목적지 노드 k
x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)