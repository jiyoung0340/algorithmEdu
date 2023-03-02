from collections import deque

n, k = map(int, input().split())

arr = deque()
for i in range(n):
    arr.append(i + 1)

res = []
while arr:
    for _ in range(k - 1):
        arr.append(arr.popleft())
    res.append(arr.popleft())

print(str(res).replace('[', '<').replace(']', '>'))