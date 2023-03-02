import sys

n = int(sys.stdin.readline())
buildings = []
for _ in range(n):
    buildings.append(int(sys.stdin.readline()))

stack = []
res = 0
for i in buildings:
    while stack and i >= stack[-1]:
        stack.pop()
    stack.append(i)
    res += len(stack) - 1

print(res)