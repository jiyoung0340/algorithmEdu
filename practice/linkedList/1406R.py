str = list(input())
n = int(input())
spot = len(str)

for _ in range(n):
    com = list(input().split())
    if com[0] == 'L':
        if spot > 0:
            spot -= 1
    elif com[0] == 'D':
        if spot < len(str):
            spot += 1
    elif com[0] == 'B':
        if spot > 0:
            str.remove(str[spot - 1])
            spot -= 1
    else:
        str.insert(spot, com[1])
        spot += 1

for i in str:
    print(i, end='')

