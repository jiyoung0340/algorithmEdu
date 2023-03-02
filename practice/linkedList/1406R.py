# # 내가 푼 방법 : 시간 초과
# # insert(), remove() => O(n)
# str = list(input())
# n = int(input())
# spot = len(str)
#
# for _ in range(n):
#     com = list(input().split())
#     if com[0] == 'L':
#         if spot > 0:
#             spot -= 1
#     elif com[0] == 'D':
#         if spot < len(str):
#             spot += 1
#     elif com[0] == 'B':
#         if spot > 0:
#             str.remove(str[spot - 1])
#             spot -= 1
#     else:
#         str.insert(spot, com[1])
#         spot += 1
#
# for i in str:
#     print(i, end='')

# append(), pop() => O(1)
import sys

str1 = list(sys.stdin.readline().rstrip())
str2 = []
n = int(input())

for _ in range(n):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if len(str1) != 0:
            str2.append(str1.pop())
        else:
            continue
    elif command[0] == 'D':
        if len(str2) != 0:
            str1.append(str2.pop())
        else:
            continue
    elif command[0] == 'B':
        if len(str1) != 0:
            str1.pop()
        else:
            continue
    else:
        str1.append(command[1])

str1.extend(reversed(str2))
for i in str1:
    print(i, end='')

#########################################################
x = ['abc', 'def', 'ghi']
y = ['123', '456', '789']
s = '12345'

# x.append(y) # ['abc', 'def', 'ghi', ['123', '456', '789']]
# x.extend(y) # ['abc', 'def', 'ghi', '123', '456', '789']
# x.append(s) # ['abc', 'def', 'ghi', '12345']
# x.extend(s) # ['abc', 'def', 'ghi', '1', '2', '3', '4', '5']

