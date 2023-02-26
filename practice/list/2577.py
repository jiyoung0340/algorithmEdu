res = 1
for i in range(3):
    n = int(input())
    res *= n

arr = [0] * 10
for i in str(res):
    arr[int(i)] += 1

for i in range(len(arr)):
    print(arr[i])