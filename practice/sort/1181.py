n = int(input())

param = []
for i in range(n):
    s = input()
    if s not in param:
        param.append(s)

param.sort()
res = sorted(param, key=lambda x: len(x))

for r in res:
    print(r)
