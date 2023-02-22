# 최소 공통 조상(Lowest Common Ancestor) 문제 : O(NM)
# 최소 공통 조상 문제는 두 노드의 공통된 조상 중에서 가장 가까운 조상을 찾는 문제이다.
# 1. 모든 노드에 대한 깊이를 계산 (DFS 사용)
# 2. 최소 공통 조상을 찾을 두 노드를 확인
#     1) 먼저 두 노드의 깊이가 동일하도록 거슬러 올라감
#     2) 이후에 부모가 같아질 때까지 반복적으로 두 노드의 부모 방향으로 거슬로 올라감
# 3. 모든 LCA(a, b) 연산에 대해 2번 과정을 반복
#
# ex. N(2 <= N <= 50000)개의 정점으로 이루어진 트리가 있고 각 정점은 1번부터 N번까지 번호가 매겨져 있으며 루트는 1번이다.
# 두 노드의 쌍 M(1 <= M <= 10000)개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇번인지 출력하라.

import sys
sys.setrecursionlimit(int(1e5)) # 런타임 오류 피하기
n = int(input())

parent = [0] * (n + 1) # 부모 노드 정보
d = [0] * (n + 1) # 각 노드까지의 깊이
c = [0] * (n + 1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)] # 그래프(graph) 정보

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작해 깊이를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구했다면 넘기기
            continue
        parent[y] = x
        dfs(y, depth + 1)

# A와 B의 최소 공통 조상 찾는 함수
def lca(a, b):
    while d[a] != d[b]: # 먼저 깊이가 동일하도록
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[a]

    while a != b: # 노드가 같아지도록
        a = parent[a]
        b = parent[b]
    return a

dfs(1, 0) # 루트 노드는 1번 노드

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))

# 개선하기 : 각 노드가 거슬러 올라가는 속도를 빠르게 만들자! O(MlogN)
# 2의 제곱 형태로 거슬러 올라가면 O(logN)의 시간 복잡도를 보장한다 = 메모리를 좀 더 사용해 각 노드에 대해 2^i번째 부모에 대한 정보를 기록한다.
# 다이나믹 프로그래밍을 이용해 시간 복잡도 개선!(세그먼트 트리를 이용하는 방법도 존재함)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5)) # 런타임 오류 피하기
LOG = 21 # 2^20 = 1000000

n = int(input())

parent = [[0] * LOG for _ in range(n + 1)] # 부모 노드 정보
d = [0] * (n + 1) # 각 노드까지의 깊이
c = [0] * (n + 1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)] # 그래프(graph) 정보

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작해 깊이를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구했다면 넘기기
            continue
        parent[y] = x
        dfs(y, depth + 1)

# 전체 부모 관계를 설정하는 함수
def set_parent():
    dfs(1, 0) # 루트 노드는 1번노드
    for i in range(1, LOG):
        for j in range(1, n + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]

# A와 B의 최소 공통 조상 찾는 함수
def lca(a, b):
    # b가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a

    for i in range(LOG - 1, -1, -1): # 먼저 깊이가 동일하도록
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]

    if a == b: # 부모가 같아지도록
        return a

    for i in range(LOG - 1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0] # 이후에 부모가 찾고자 하는 조상

set_parent()

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
