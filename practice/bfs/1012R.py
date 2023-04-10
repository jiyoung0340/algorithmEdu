from collections import deque
import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def loc(res):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j, graph)
                count += 1

    res.append(count)


def bfs(x, y, graph):
    deq = deque()
    deq.append((x, y))

    while deq:
        x, y = deq.popleft()
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or len(graph) <= nx or len(graph[0]) <= ny or graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                deq.append((nx, ny))


t = int(sys.stdin.readline().rstrip())
res = []
for _ in range(t):
    loc(res)
for r in res:
    print(r)


