a, b = map(int, input().split())
if a > b :
    a, b = b, a
diff = b - a
data = []

for i in range(1, diff):
    data.append(a + i)

print(len(data))
for i in range(len(data)):
    print(data[i], end = " ")