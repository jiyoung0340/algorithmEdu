import sys

k = int(sys.stdin.readline())

arr = []
for i in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        arr.pop()
    else:
        arr.append(n)

res = 0
for i in arr:
    res += i
print(res)