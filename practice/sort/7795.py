##########################################################
# 이진 탐색을 위한 라이브러리 bisect
# bisect_left(a, x) : a에 x를 정렬한 상태를 유지하며 삽입할 위치를 찾는 함수.
# x가 a에 이미 있으면, 삽입 위치는 기존 항목의 앞(=왼쪽)에 위치함.
# A 집합의 원소 a가 B 집합에 삽입 될 위치 인덱스 = a보다 작은 B의 원소 갯수
##########################################################
from bisect import bisect_left


def sol():
    count = 0
    number_a, number_b = map(int, input().split())
    n = list(map(int, input().split()))
    m = list(map(int, input().split()))
    n.sort()
    m.sort()

    for a in n:
        count += bisect_left(m, a)
    return count


t = int(input())
for _ in range(t):
    print(sol())

