arr = []
for i in range(7):
    arr.append(int(input()))

s = 0
brr = []

for i in range(7):
    if arr[i] % 2 == 1:
        s += arr[i]
        brr.append(arr[i])

if len(brr)== 0:
    print("-1")
else:
    print(s)
    print(min(brr))