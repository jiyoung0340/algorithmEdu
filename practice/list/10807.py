l = int(input())
data = list(map(int, input().split()))
n = int(input())

count = 0
for i in range(l):
    if data[i] == n:
        count += 1

print(count)