# Q1. 두 배열의 원소 교체
# N : 배열의 길이
# K : 총 바꿔치기할 연산의 수
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))