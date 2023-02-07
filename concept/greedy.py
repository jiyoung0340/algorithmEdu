# 거스름돈 문제 예시 답안
n1 = 1260
count = 0

array = [500, 100, 50, 10]
for coin in array:
    count += n1 // coin
    n1 %= coin

print(count)
# 화폐의 종류가 k라고 할 때, 소스코드의 시간 복잡도는 O(k)이다.
# 따라서 거슬러줘야하는 금액과 무관하게 동전의 종류에만 영향을 받음

# 1이 될 때까지
n2 = 25
k = 3
count = 0
while(n2 > 1):
    if(n2 % k == 0):
        n2 //= k
        count+=1
    else:
        n2 -= 1
        count +=1
    # if(n2 == 1): break
# 1이 될 때까지 - 2
# 반복문이 돌 때마다 n을 k로 나누는 연산이 진행되기 때문에 더 빠르게 진행됨
n, k = map(int, input().split())
result = 0
while True:
    # N이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n //k) * k
    result += (n - target)
    n = target
    # N이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k :
        break
    result += 1
    n //= k
# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)

# 곱하기 혹은 더하기
s = '02984'
res = int(s[0])

for i in range(1, len(s)):
    i1 = int(s[i])
    if i1 <= 1 or res <= 1:
       res += i1
    else:
        res *= i1

print(res)

# 모험가 길드 3 2 2 2 1
n = int(input())
data = list(map(int, input().split()))
data.sort()

res = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        res += 1
        count = 0

print(res)