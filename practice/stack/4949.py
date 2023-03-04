# sys.stdin.readLine()과 input()을 적절히 사용하자

while True:
    exInput = input()
    # while문 종료 조건
    if exInput == '.':
        break
    stack = []
    flag = True
    for ex in exInput:
        if ex in ['(', '[']:
            stack.append(ex)
        elif ex == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
        elif ex == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break

    if flag and not stack:
        print('yes')
    else:
        print('no')
