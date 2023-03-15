import sys

n = int(sys.stdin.readline())
arr = [0] * 10000

for _ in range(n):
    k = int(sys.stdin.readline())
    arr[k-1] += 1

for i in range(len(arr)):
    if arr[i] > 0:
        for _ in range(arr[i]):
            print(i + 1)