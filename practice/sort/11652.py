###########################################################
# Dictionary 자료형
# key, value 쌍의 집합으로 중복된 키를 허용하지 않는다.
# dict() 로 빈 딕셔너리를 생성한다.
# key 값을 통해 value값을 얻는다
# dictionary 를 순차적으로 조회하기 위해 items()라는 함수를 사용한다.
# items() 함수?
# key-value 쌍의 dictionary를 튜플 리스트로 반환해준다.
###########################################################

import sys

n = int(sys.stdin.readline())
cards = dict()

for _ in range(n):
    c = int(sys.stdin.readline())
    if c in cards:
        cards[c] = cards[c] + 1
    else:
        cards[c] = 1

max_value = 0
max_key = 0
for k, v in cards.items():
    if v > max_value:
        max_value = v
        max_key = k
    elif v == max_value and k < max_key:
        max_key = k
print(max_key)
