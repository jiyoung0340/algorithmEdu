import sys

n = int(sys.stdin.readline())
loc_list = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    loc_list.append((x, y))
loc_list = sorted(loc_list)

for loc in loc_list:
    print(loc[0], loc[1], end="\n")