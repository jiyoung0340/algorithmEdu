from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    deq = deque()
    deq.append((x, y))
    graph[x][y] = 0
    area = 1

    while deq:
        a, b = deq.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                deq.append((nx, ny))
                area += 1
    return area


n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

res = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            res.append(bfs(i, j))

if res:
    print(len(res))
    print(max(res))
else:
    print(len(res))
    print(0)


