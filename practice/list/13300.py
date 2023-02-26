n, k = map(int,input().split())

res = [[0 for _ in range(2)] for _ in range(6)]
r = 0
for _ in range(n):
    a, b = map(int, input().split())
    res[b - 1][a] += 1
    if res[b - 1][a] == k:
        r += 1
        res[b - 1][a] = 0

for i in res:
    if i[0] >= 1:
        r += 1
    if i[1] >= 1:
        r += 1
print(r)
