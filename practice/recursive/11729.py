n = int(input())

def hanoi(k, start, end):
    if k == 1:
        print(start, end)
        return 1
    else:
        hanoi(k - 1, start, 6 - (start + end))
        print(start, end)
        hanoi(k - 1, 6 - (start + end), end)

sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(n, 1, 3)
