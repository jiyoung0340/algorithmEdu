# 상하좌우 문제
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L','R','U','D']

#  이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # 공간을 벗어나면 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        # 이동 수행
        x, y = nx, ny
print(x, y)

# 시각문제
h = int(input())

count = 0
for i in range(h + 1):      # 시
    for j in range(60):     # 분
        for k in range(60): # 초
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

# 체스판
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
res = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당  위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8 :
        res += 1
print(res)

# 문자열 재정렬
data = input()
res = []
sum = 0
for i in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if i.isalpha():
        res.append(i)
    # 숫자의 경우 따로 더하기
    else:
        res += int(i)
res.sort() # 알파벳 오름차순 정렬
if sum != 0:
    res.append(str(sum))
# 리스트를 문자열로 변환하여 출력
print(''.join(res))