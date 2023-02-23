a, b, c = map(int, input().split(' '))

arr = [0] * 7
arr[a] += 1
arr[b] += 1
arr[c] += 1

for i in range(1, 7):
    if arr[i] == 0:
        continue
    elif arr[i] == 3:
        res = 10000 + i * 1000
        break
    elif arr[i] == 2:
        res = 1000 + i * 100
        break
    else:
        res = max(a, b, c) * 100

print(res)

# 3개뿐만이 아닌 N개를 받을 때는 어떻게 할 것인가?
