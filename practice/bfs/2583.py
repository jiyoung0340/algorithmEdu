from collections import deque


def bfs(x, y):
    q = deque()
    area = 1
    graph[x][y] = 1
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = 1
                area += 1
    resList.append(area)


m, n, k = map(int, input().split())

resList = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = list(map(int, input().split()))
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[j][i] = 1

    for i in range(n):
        for j in range(m):
            if graph[j][i] == 0:
                bfs(j, i)

print(resList)

