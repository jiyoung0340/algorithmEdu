n = int(input())

count = 0
for _ in range(n):
    exInput = input()
    stack = []
    for e in exInput:
        if stack and stack[-1] == e:
            stack.pop()
        else:
            stack.append(e)

    if not stack:
        count += 1

print(count)
