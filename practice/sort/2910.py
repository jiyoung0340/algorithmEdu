n, c = map(int, input().split())
arr = list(map(int, input().split()))
res = dict()

for a in arr:
    if a not in res:
        res[a] = 0
    res[a] += 1

res = sorted(res.items(), key=lambda x: x[1], reverse=True)

for r in res:
    for i in range(r[1]):
        print(r[0], end=" ")




