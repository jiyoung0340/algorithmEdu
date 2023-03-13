import sys
a, b, c = map(int, sys.stdin.readline().split())

def multi(x, y, z):
    if y == 1:
        return x % z;
    elif y % 2 == 0:
        return (multi(x, y//2, z) ** 2) % z
    else:
        return ((multi(x, y//2, z) ** 2) * x) % z
print(multi(a, b, c))


