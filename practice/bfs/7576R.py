from collections import deque

n, m = map(int, input().split())
box = []
for _ in range(m):
    box.append(list(map(int, input().split())))
day = 0
b = False
for i in range(m):
    for j in range(n):
        if box[i][j] == 0:
            b = True

if b:
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    deq = deque()
    res = []

    for i in range(m):
        for j in range(n):
            if box[i][j] == 1:
                deq.append((i, j))

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                deq.append((nx, ny))

    day = max(max(box)) - 1
    for i in range(m):
        for j in range(n):
            if box[i][j] == 0:
                day = -1

else:
    day = 0

print(day)
