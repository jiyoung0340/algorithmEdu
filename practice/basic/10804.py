data = [i for i in range(0, 21)]

for i in range(10):
    start, end = map(int, input().split())
    temp = data[start: end + 1]
    temp.reverse()
    for j in range(len(temp)):
        data[j + start] = temp[j]


for i in range(1, len(data)):
    print(data[i], end=" ")

