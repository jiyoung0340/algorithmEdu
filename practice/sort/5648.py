######################################################################################
# list의 요소를 인덱스로 제거하기
# del list[index]
#
# 문자열을 역순으로 출력하기
# print(strEx[::-1])
#
# 숫자를 문자열로 바꾸기
# str(intEx)
######################################################################################
arr = []
while True:
    values = map(int, input().split())
    for v in values:
        arr.append(v)
    if arr[0] + 1 == len(arr):
        break

del arr[0]
for i in range(len(arr)):
    arr[i] = int(str(arr[i])[::-1])

arr.sort()
for a in arr:
    print(a)