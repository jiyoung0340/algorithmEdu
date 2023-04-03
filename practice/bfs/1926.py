#######################################################
#          x-1, y
#            |
# x, y-1 ㅡ x, y ㅡ x, y+1
#            |
#          x+1, y
#######################################################

from collections import deque

h, w = map(int, input().split())
graph = []

for _ in range(h):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    count = 1

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                count += 1
    return count


paint = []
for i in range(h):
    for j in range(w):
        if graph[i][j] == 1:
            paint.append(bfs(i, j))

if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))
