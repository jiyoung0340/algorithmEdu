data = []
for _ in range(9):
    data.append(int(input()))

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if sum(data) - data[i] - data[j] == 100:
            data.remove(data[j])
            data.remove(data[i])
            data.sort()
            break

for i in range(len(data)):
    print(data[i])