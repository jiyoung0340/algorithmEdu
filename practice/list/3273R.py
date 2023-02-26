from itertools import combinations

leng = int(input())
data = sorted(list(map(int, input().split())))

s = int(input())
count = 0

left, right =0, leng - 1
while left < right:
    if data[left] + data[right] == s:
        count += 1
        left += 1
    elif data[left] + data[right] < s:
        left += 1
    else:
        right -= 1

print(count)