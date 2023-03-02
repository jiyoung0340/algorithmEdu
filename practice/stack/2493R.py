# 내가 푼 방법 => 메모리 초과
# import sys
#
# n = int(sys.stdin.readline())
# tower = list(sys.stdin.readline().split())
#
# temp = []
# current = len(tower) - 1
# res = [0] * n
# for _ in tower:
#     top = tower.pop()
#     while tower:
#         if top <= tower[-1]:
#             res[current] = len(tower)
#             current -= 1
#             if temp:
#                 tower.extend(reversed(temp))
#             break
#         else:
#             temp.append(tower.pop())
# for i in res:
#     print(i, end=' ')

# 튜플을 이용
# 메모리 초과 => 필요없는 데이터를 저장한다는 것!
import sys

n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
stack = []
answer = [0] * n

for i in range(n):
    t = tower[i]
    while stack and t >= stack[-1][1]:
        stack.pop()
    if stack:
        answer[i] = stack[-1][0]
    stack.append((i + 1, tower[i]))

for i in answer:
    print(i, end=" ")