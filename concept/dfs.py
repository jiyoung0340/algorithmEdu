# DFS 메서드 정의
def dfs(graph, v, visited):
    #  현재 노드 방문처리
    visited[v] = True
    print(v, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현한 리스트
visited = [False] * 9 # 0번 인덱스를 사용하지 않으려고 일부러 9로 함
# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

# 음료수 얼려 먹기
def ice_dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0 :
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상 하 좌 우 위치들도 모두 재귀적으로 호출
        ice_dfs(x-1, y)
        ice_dfs(x, y-1)
        ice_dfs(x+1, y)
        ice_dfs(x, y+1)
        return True
    return False

n, m = map(int, input().split())
# 2차원 리스트 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
# 모든 노드에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
print(result)