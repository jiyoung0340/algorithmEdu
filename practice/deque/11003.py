# 시간초과 -> min()의 경우 O(n) 의 시간복잡도로 해당 문제에 적절하지않다!

from collections import deque
import sys

n, l = map(int, sys.stdin.readline().split())
exInput = list(map(int, sys.stdin.readline().split()))
q = deque()
answer = []
for i in range(n):
    while q and exInput[i] < q[-1][1]:
        q.pop()
    if q and q[0][0] <= i - l:
        q.popleft()
    q.append((i, exInput[i]))
    answer.append(q[0][1])
for a in answer:
    print(a, end=' ')
