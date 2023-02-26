str = input()
res = [0] * 26
for c in str:
    res[ord(c) - 97] += 1

for i in range(len(res)):
    print(res[i], end=" ")