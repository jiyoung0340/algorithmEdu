from collections import deque
import sys

n = int(sys.stdin.readline())
res = deque()
for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':
        res.appendleft(command[1])
    elif command[0] == 'push_back':
        res.append(command[1])
    elif command[0] == 'pop_front':
        if res:
            print(res.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if res:
            print(res.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(res))
    elif command[0] == 'empty':
        if res:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if res:
            print(res[0])
        else:
            print(-1)
    else:
        if res:
            print(res[-1])
        else:
            print(-1)
