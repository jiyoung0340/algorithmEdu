import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(int(input()))

list.sort(arr)

for i in range(n):
    print(arr[i])