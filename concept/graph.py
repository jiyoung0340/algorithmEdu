############################################반복##############################################################
# 서로소 집합 자료구조
def find_parent(parent, x): # 특정 원소가 속한 집합 찾기
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 찾기(Find)함수 최적화 -> 경로 압축 : 찾기(Find)함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 바로 갱신한다.
def find_parent_pc(parent, x):
    if parent[x] != x:
        parent[x] = find_parent_pc(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b): # 두 원소가 속한 집합 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split()) # 노드의 개수와 간선(Union 연산)의 개수 입력 받기
parent = [0] * (v + 1)

for i in range(1, v + 1): # 부모를 자기 자신으로 초기화
    parent[i] = i
##########################################################################################################

# 서로소 집합 자료구조
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print("각 원소가 속한 집합: ", end="")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")

print()

print('부모 테이블: ', end="")
for i in range(1, v + 1):
    print(parent[i], end= ' ')

# 사이클 판별
cycle = False
for i in range(e):
    a, b = map(int, input().split())
    if find_parent_pc(parent, a) == find_parent_pc(parent, b): # 사이클이 발생한 경우 종료
        cycle = True
        break
    else: # 사이클이 발생하지 않았다면 합집합(Union) 연산 수행
        union_parent(parent, a, b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 발생X")

# 크루스칼 알고리즘
edges = [] # 모든 간선을 담을 리스트
result = 0 # 최종 비용을 담을 변수

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b)) # 비용순으로 정렬하기 위해 튜플의 첫번째 원소를 비용으로 설정

edges.sort() # 튜플의 경우 첫번째 원소를 기준으로 정렬해줌

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않은 경우에만 집합에 포함
    if find_parent_pc(parent, a) != find_parent_pc(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

# 큐를 이용한 위상 정렬 알고리즘
from collections import deque

v, e = map(int, input().split()) # 노드의 개수와 간선의 개수
indegree = [0] * (v + 1) # 모든 노드에 대한 진입차수는 0으로 초기화
graph = [[] for i in range(v + 1)] # 각 노드에 연결된 간선의 정보를 담기 위한 연결 리스트 초기화

for _ in range(e): # 방향 그래프의 모든 간선 정보 입력 받기
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    indegree[b] += 1 # 진입 차수를 1 증가

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    for i in range(1, v + 1): # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
        if indegree[i] == 0:
            q.append(i)

    while q: # 큐가 빌 때까지 반복
        now = q.popleft() # 큐에서 원소꺼내기
        result.append(now)
        for i in graph[now]: # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
            indegree[i] -= 1
            if indegree[i] == 0: # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                q.append(i)

    for i in result: # 위상 정렬을 수행한 결과 출력
        print(i, end=' ')

topology_sort()