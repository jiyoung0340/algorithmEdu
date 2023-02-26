n = int(input())

data = [0] * 26
strfry = [0] * 26
res = [] * n
for _ in range(n):
    flag = "Possible"
    d, f = input().split()


    for i in d:
        data[ord(i) - ord('a')] += 1
    for i in f:
        strfry[ord(i) - ord('a')] += 1

    for i in range(len(data)):
        if data[i] != strfry[i]:
            flag = "Impossible"
            break
    res.append(flag)



for i in range(n):
    print(res[i])
