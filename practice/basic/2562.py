data = []

for i in range(9):
    n = int(input())
    data.append(n)

m = max(data)
print(m)
print(data.index(m) + 1)
