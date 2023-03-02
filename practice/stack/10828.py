# deque로 안해도 되는부분... => 시간초과 문제는 input()대신 sys를 이용하도록!
from collections import deque
import sys

a = int(sys.stdin.readline())
stack = deque()

for _ in range(a):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'top':
        if stack:
            top = stack.pop()
            print(top)
            stack.append(top)
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack.pop())
        else:
            print(-1)
