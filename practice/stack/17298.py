import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

stack = []
answer = [-1] * n
for i in range(n):
    while stack and stack[-1][1] < arr[i]:
        answer[stack[-1][0]] = arr[i]
        stack.pop()
    stack.append((i, arr[i]))

for a in answer:
    print(a, end=" ")