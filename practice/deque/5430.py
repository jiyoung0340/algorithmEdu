import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    command = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())

    if n == 0:
        print('error')
        continue
    target = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    res = True
    rcount = 0
    for com in command:
        if com == 'R':
            rcount += 1
        else:
            if target and rcount % 2 == 0:
                target.popleft()
            elif target and rcount % 2 != 0:
                target.pop()
            else:
                res = False
                break

    if res and rcount % 2 != 0:
        target.reverse()
        print("[" + ",".join(target) + "]")
    elif res and rcount % 2 == 0:
        print("[" + ",".join(target) + "]")
    else:
        print('error')
