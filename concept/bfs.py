from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # Queue 구현을 위해 deque라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

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
visited = [False] * 9
# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

# 미로찾기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def maze(x, y) :
    # Queue 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로를 벗어난 경우 무시
            if nx < 0 or nx >= n  or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
# 가장 오른쪽 아래까지의 최단거리 반환
    return graph[n - 1][m - 1]

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))
print(bfs(0, 0))