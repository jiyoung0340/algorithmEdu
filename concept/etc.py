# 소수 M1.
def is_prime_number1(x) :
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

# 소수 M2.
import math
def is_prime_number2(x) :
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# 에라토스테네스의 체
import math

n = 1000
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n))+ 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 결과 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')

# 투 포인터
n = 5 # 데이터의 갯수 N
m = 5 # 찾고자 하는 부분 합 M
data = [1,2,3,2,5] # 전체 수열

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n: # end 를 가능한 만큼 이동시키기
        interval_sum += data[end]
        end += 1
    if interval_sum == m: # 부분합이 m일 때 카운트 증가
        count += 1
    interval_sum -= data[start]

print(count)

# 접두사 합(Prefix Sum)
n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

left = 3
right = 4
print(prefix_sum(right) - prefix_sum[left - 1])