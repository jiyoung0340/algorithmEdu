# 피보나치 (재귀 함수 사용)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)
print(fibo(4))

# 피보나치 (탑다운)
# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현 - 탑다운 다이나믹 프로그래밍
def fibo(x):
    # 종료 조건 : 1 또는 2일 때 1 반환
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적이 있는 문제면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 다라 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x-2)
    return d[x]

# 피보나치(바텀업)
# 앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 박복문으로 구현 - 바텀없 다이나믹 프로그래밍
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

# Q. 개미전사
n = int(input())
array = list(map(int, input().split('')))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100
# 다이나믹 프로그래밍 바텀업 진행
d[0]= array[0]
d[1]= max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i-2] + array[i])

# Q. 1로 만들기
x = int(input())
# DP테이블 초기화
d = [0] * 30001

# 바텀업 진행
for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    # 현재의 수가 3로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

# Q. 효율적인 화폐 구성
n, m = map(int, input().split())
# N개의 화폐 단위 정보 입력받기
array = []
for i in range(n):
    array.append(int(input()))
d = [1001] * (m + 1)
d[0] = 0
for i in range(n): # i: 각각의 화폐단위
    for j in range(array[i], m + 1): # 각각의 금액
        if d[j - array[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])



