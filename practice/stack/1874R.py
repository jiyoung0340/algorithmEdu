# a = [1,2,3,4] 일때 a[-1] = 4
import sys

n = int(sys.stdin.readline())
stack = []
answer = []
current = 1

flag = True
for i in range(n):
    num = int(sys.stdin.readline())
    while current <= num:
        stack.append(current)
        answer.append('+')
        current += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        flag = False
        break

if flag:
    for i in answer:
        print(i)