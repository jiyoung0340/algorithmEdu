n = int(input())
arr = list(map(int, input().split()))

y, m = 0, 0
for i in range(len(arr)):
    y += (arr[i] // 30 + 1) * 10
    m += (arr[i] // 60 + 1) * 15

if m < y :
    print("M", m)
elif y < m :
    print("Y", y)
else:
    print("Y M", m)

