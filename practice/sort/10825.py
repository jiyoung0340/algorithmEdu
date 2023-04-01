##########################################################
# lambda 함수를 사용해서 sorted() 함수의 정렬 조건 추가하기
# sorted(list, key=lambda x: func(x)) : func(x)를 기준으로 list를 정렬한다.
# key를 여러개 설정하면 튜플로
# sorted(list, key=lambda x: (x[1], x[2], ..., x[0])
# key의 역순으로 설정하고자 하면
# sorted(list, key=lambda x: -x[1])
##########################################################

n = int(input())

res = []
for _ in range(n):
    l = list(input().split())
    t = (l[0], int(l[1]), int(l[2]), int(l[3]))
    res.append(t)

res = sorted(res, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for r in res:
    print(r[0])
