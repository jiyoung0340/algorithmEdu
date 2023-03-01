a = list(input())
b = list(input())

acount = [0] * 26
bcount = [0] * 26

for i in range(len(a)):
    acount[ord(a[i]) - ord('a')] += 1
for i in range(len(b)):
    bcount[ord(b[i]) - ord('a')] += 1

count = 0
for i in range(26):
    a, b = acount[i], bcount[i]
    if a < b :
        a, b = b, a
    count += a - b

print(count)

