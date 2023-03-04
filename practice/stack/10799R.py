# 코드구현보다 문제에대한 이해력이 더 필요하다
bar = input()

stack = []
count = 0
for i in range(len(bar)):
    if bar[i] == '(':
        stack.append(bar[i])
    elif bar[i] == ')' and bar[i - 1] == '(': # 레이져
        stack.pop()
        count += len(stack)
    else:
        stack.pop()
        count += 1
print(count)