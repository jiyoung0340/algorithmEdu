import sys
from builtins import range

n = int(sys.stdin.readline())

tuple_list = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    t = int(age), name
    tuple_list.append(t)

result_list = sorted(tuple_list, key=lambda tu: tu[0])

for i in range(n):
    print(result_list[i][0], result_list[i][1], end="\n")