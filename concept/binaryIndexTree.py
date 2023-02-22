# 바이너리 인덱스 트리(Binary Index Tree:BIT)
# 2진법 인덱스 구조를 활용해 구간 합 문제를 효과적으로 해결해 줄 수 있는 자료구조로 펜윅 트리라고도 함.
#
# * 정수를 2진수로 표기할 때, 음수의 경우는 양수의 2진 표기를 1->0, 0->1 로 바꾼 후, 1을 더해준다.
# 이를 토대로 2진수에서 0이 아닌 마지막 비트를 찾는 방법은 K & -K를 해주면 찾을 수 있다.
# K & -K
k = 8

for i in range(n+1):
    print(i, '의 마지막 비트:', (i & -i))

# ex. 데이터의 업데이트가 가능한 상황에서의 구간 합 문제
# 어떤 N개의 수가 있는데 중간에 수의 변경이 번번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다.
# 예를 들어 1,2,3,4,5라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지의 합을 구하라 하면 17을 출력한다
# 그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째 부터 5번째 합을 구하라고 한다면 12를 출력한다.
# 데이터의 개수 : N ( 1 <= n <= 1000000)
# 데이터 변경 횟수 : M ( 1 <= M <= 10000)
# 구간 합 계산 횟수 : K ( 1 <= K <= 10000)

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split()) # 데이터의 개수(n), 변경 횟수(m), 구간 합 계산 횟수(k)

arr = [0] * (n + 1)
tree = [0] * (n + 1)

# i번째 수까지의 누적 합을 계산하는 함수
def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i & -i) # 0이 아닌 마지막 비트만큼 빼가면서 이동
    return result

def update(i, dif): # i번째 수를 dif만큼 더하는 함수
    while i <= n:
        tree[i] += dif
        i += (i & -i)

def interval_sum(start, end): # start부터 end까지 구간 합을 구하는 함수
    return prefix_sum(end) - prefix_sum(start - 1)

for i in range(1, n + 1):
    x = int(input())
    arr[i] = x
    update(i, x)

for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1: # 업데이트 연산인 경우
        update(b, c - arr[b]) # 바뀐 크기 dif 적용
        arr[b] = c
    else: # 구간 합 연산인 경우
        print(interval_sum(b, c))