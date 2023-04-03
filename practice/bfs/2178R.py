from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(input()))))


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
deq = deque()


def bfs(a, b):
    deq.append((a, b))
    graph[a][b] = 0
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                deq.append((nx, ny))
                graph[nx][ny] += graph[x][y]


bfs(0, 0)
print(graph[n-1][m-1] + 1)