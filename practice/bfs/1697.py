from collections import deque

dist = [0] * 100001
n, k = map(int, input().split())

deq = deque()
deq.append(n)

while deq:
    a = deq.popleft()

    if a == k:
        print(dist[a])
        break

    for i in (a-1, a+1, a*2):
        if 0 <= i <= 100000 and not dist[i]:
            deq.append(i)
            dist[i] = dist[a] + 1



