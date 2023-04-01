from builtins import range

s = input()
s_list = list(s)
res = []

for j in range(len(s_list)):
    s = ""
    for i in range(j, len(s_list)):
        s += s_list[i]
    res.append(s)

res.sort()
for r in res:
    print(r)