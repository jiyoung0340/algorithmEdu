# 파이썬 이진 탐색 라이브러리
from bisect import bisect_left, bisect_right
a = [1, 2, 4, 4, 8]
x = 4
bisect_left(a, x) # 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환
bisect_right(a, x) # 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스 반환

# 특정 범위에 속하는 데이터 개수 구하기
# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))
# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))

# Q1. 떡볶이 떡
n, m = map(int, input().split(' '))
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점
start = 0
end = max(array)

# 이진 탐색 수행
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡 양 계산
        if x > mid:
            total += (x - mid)
    # 떡의 양이 부족한 경우 더 많이 자르기 => 왼쪽 부분 탐색
    if total < m :
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기 => 오른쪽 부분 탐색
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result 기록
        start = mid + 1

print(result)

# Q. 정렬된 배열에서 특정 수의 개수 구하기
n, x = map(int, input().split(' '))
array = list(map(int, input().split()))

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

count = count_by_range(array, x, x)
if count > 0:
    print(count)
else:
    print(-1)
