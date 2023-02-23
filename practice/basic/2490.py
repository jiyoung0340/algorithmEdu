def res(arr):
    if sum(arr) == 0:
        print("D")
    elif sum(arr) == 3:
        print("A")
    elif sum(arr) == 2:
        print("B")
    elif sum(arr) == 1:
        print("C")
    else:
        print("E")

for i in range(3):
    a = list(map(int, input().split()))
    res(a)

