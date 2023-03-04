n = int(input())

for _ in range(n):
    exInput = input()
    stack = []
    flag = True
    for e in exInput:
        if e == '(':
            stack.append(e)
        elif stack and e == ')':
            stack.pop()
        else:
            flag = False

    if flag and not stack:
        print('YES')
    else:
        print('NO')
