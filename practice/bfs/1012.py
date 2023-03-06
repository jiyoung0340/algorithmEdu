from collections import deque

t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, graph):
    q.append((x, y))
    graph[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0

for _ in range(t):
    m, n, k = map(int, input().split())
    q = deque()
    count = 0
    field = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        field[a][b] = 1

    for a in range(m):
        for b in range(n):
            if field[a][b] == 1:
                bfs(a, b, field)
                count += 1

print(count)

