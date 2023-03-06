from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

queue = deque()
day = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

for i in range(n):
    for j in range(m):
        if graph[j][i] == 1:
            bfs(j, i)

for i in graph:
    for j in i:
        # 토마토를 익히지 못했다면 -1 출력
        if j == 0:
            print(-1)
            exit(0)
    # 다 익혔다면 최댓값이 정답
    day = max(day, max(i))
# 처음 시작을 1로 했으니 1을 빼준다.
print(day - 1)