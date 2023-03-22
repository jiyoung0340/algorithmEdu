# a.sort() # a 리스트를 정렬(숫자 < 대문자 < 소문자) return 없음
# sorted(a) # 정렬된 a리스트를 반환 (a 리스트는 변화 없음!)
# list(str) # string to char Array
# s.isdigit() # 해당 문자열(s)가 숫자이면 True 반환 아니면 False 반환
# sys.stdin.readline().rstrip() # readline()으로 입력을 받을경우 마지막에 enter(\n)도 입력되니 조심

import sys

n = int(sys.stdin.readline())
arr = [0] * n
for i in range(n):
    arr[i] = sys.stdin.readline().rstrip()

def compare_by_sum(a):
    res = 0
    for i in a:
        if i.isdigit():
            res += int(i)
    return res

arr.sort(key=lambda x:(len(x), compare_by_sum(x) , x))

for i in arr:
    print(i)