############################## 리스트 ##############################
array = [i * i for i in range(10)]

n = 4
m = 3
# _ : 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때
array2 = [[0] * m for _  in range(n)]

# append() : 리스트에 원소를 하나 삽입할 때 => O(1)
# sort() => O(Nlogn)
#     변수명.sort() : 오름차순으로 정렬
#     변수명.sort(reverse=true) : 내림차순 정렬
# reverse() : 원소의 순서를 뒤집어 놓는다. => O(N)
# insert(삽입할 위치 인덱스, 삽입할 값) : 특정한 인덱스 위치에 삽입 => O(N)
# count(값) : 특정 값을 가지는 데이터의 개수 => O(N)
# remove(값) : 특정 값을 갖는 원소 제거/ 여러개면 하나만 제거 => O(N)

# remove_list 에 포함되지 않은 값만을 저장
a =  [1,2,3,4,5,5,5]
remove_list = {3,5}
result = [i for i in a if i not in remove_list]

############################## 튜플 ##############################
# 리스트와 유사하지만 튜플은 한 번 선언된 값을 변경할 수 없음.
# () 사용
# 공간 효율적
# 서로 다른 성질의 데이터를 묶어서 관리할 때,
# ex. 최단 경로 알고리즘에서 (비용, 노드 번호)의 형태로 자주사용
# 데이터 나열을 해싱의 키 값으로 사용해야 할 때 -> 튜플은 변경불가능하므로 리스트와 다르게 키 값으로 사용될 수 있다.
# 리스트보다 메모리를 효율적으로 사용해야할 때

############################## 사전 자료형 ##############################
# 키와 값의 쌍을 데이터로 가지는 자료형
# 원하는 변경 불가능한 자료형을 키로 사용할 수 있다.
# 파이썬의 사전자료형은 해시 테이블을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리 가능함
# keys() : 키 데이터만 뽑아서 리스트로 이용
# values() : 값 데이터만 뽑아서 리스트로 이용
data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['딸기'] = 'berry'

if '사과' in data:
    print('oo')

############################## 집합자료형 ##############################
# 중복 허용 X, 순서가 없음
# 리스트 혹은 문자열을 이용해서 초기화 가능함 -> set() 사용
# 집합 자료형 초기화 방법1
data = set([1,1,2,3,4,4,4,5])
# 집합 자료형 초기화 방법2
data2 = {6,6,6,7,8,9,10}
# 합집합
print(data | data2)
# 교집합
print(data & data2)
# 차집합
print(data - data2)
# 추가
data.add(33)
# 여러개 추가
data.update([6,7])
# 제거
data.remove(33)

# 사전자료형/집합자료형 => 순서가 없음
# 사전 사료형은 key, 집합 자료형은 원소를 이용해 조회

############################## 입출력 방식 ##############################
# input() : 한 줄의 문자열을 입력 받는 함수
# map() : 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용

# 데이터를 공백을 기준으로 구분해서 입력을 받은 다음에 모두 정수형으로 변환후 리스트로 만들어줌.
list(map(int, input().split()))
# 리스트의 원소가 많지 않을 경우, 굳이 리스트로 지원할 필요 없음.
a, b, c = map(int, input().split())
# unpack 오류 : 3개의 원소를 입력받고자 하는데 그 이상의 데이터를 입력받은 경우

# sys.stdin.readline() => 입력받을 데이터가 너무 많을 경우 사용!
# 입력을 최대한 빨리 받아야하는 경우 사용, 입력 후 엔터가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용
import sys
data = sys.stdin.readline().rstrip()
print(data)

# 표준 출력 방식
print()
# 각 변수를 콤마를 이용해 띄어쓰기로 구분하여 출력할 수 있음
# 기본적으로 출력 이후에 줄 바꿈 수행 -> 원치않을 경우 end속성 사용
# 정수형은 str로 변환 필수
print(7, end=" ")
answer = 7
print("정답은 " + str(answer))
# f-string
# 문자열 앞에 접두사 'f'를 붙여 사용
# 중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있다.
print(f"정답은 {answer}")

############################## 조건문 ##############################
x = 15
# 코드의 블록을 들여쓰기로 지정
if x >= 10:
    print("x >= 10")
    if x > 20: print(" x >= 20") # 조건문에서 실행될 소스코드가 한 줄인 경우, 줄바꿈 안해도됨
elif x == 10:
    print("x = 10")
else:
    print("x < 10")
print("end")

# 조건부 표현식
score = 80
result = "Success" if score > 80 else "Fail"
print(result)

# 논리연산자는 직관적임
if True or False:
    print("Yes")
# 부등식 복합 가능함.
if(0 < x < 30):
    print("x > 0 and x < 30")

# 기타 연산자
# 다수의 데이터를 담는 자료형을 위해 in / not in 연산자 사용 => 리스트, 튜플, 문자열, 딕셔너리 모두에서 사용 가능
x in list # 리스트 안에 x가 들어가 있을 때 참(True)
x not in str # 문자열 안에 x가 들어가 있지 않을 때 참(True)
# 아무것도 처리하고 싶지 않을 때 pass키워드
# ex. 디버깅 과정에서 일단 조건문의 형태만 만들어 놓고 조건문을 처리하는 부분은 비워놓고 싶으 ㄹ때
if x > 30:
    pass
else:
    print("x < 30")


############################## 반복문 ##############################
# while 조건문:
#     실행할 코드
# for 변수 in 리스트:
#     실행할 코드
# 연속적인 값을 차례대로 순회할 때는 range(시작 값, 끝 값+1)
# 인자를 하나만 넣으면 자동으로 시작 값은 0
for i in range(1, 10):
    result += i
print(result) # 45

# continue : 남은 코드의 실핸은 건너뛰고, 다음 반복 진행할 때,
# 1부터 9까지 홀수의 합 구하기
result = 0
for i in range(1,10):
    if i % 2 == 0:
        continue
    result += i
print(result) # 25

# break : 반복문 즉시 탈출
# 1부터 5까지 정수를 차례대로 출력
i = 1
while True:
    print("현재 :", i)
    if i == 5:
        break
    i += 1

# ex. 점수 80점 넘으면 합격
scores = [90, 85, 77, 65, 97]
for i in range(5):
    if scores[i] >= 80:
        print(i+1, "번 학생 합격")

############################## 함수 ##############################
# def 함수명(매개변수):
#     실행 코드
#     return 반환 값
# global : global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조
a = 0
b = 10
arr = [1,2,3,4,5]

def func():
    global a
    a += 1
    print(b) # 전역 변수의 값을 변경하는 것이아닌 단순 값만 참조하는 경우에는 global 키워드 사용 안해도됨.
    array.append(6) # 리스트의 내부함수를 사용할 때는 global 안해도됨
    # 단 같은 이름의 함수가 함수 내부에 선언된다면 내부 변수가 참조됨
    print(array)
for i in range(10):
    func()

print(a) # 10

# 파이썬에서 함수는 여러개의 반환값을 가질 수 있음
def operator(a, b):
    add_val = a + b
    subs_val = a - b
    mult_val = a * b
    div_val = a / b
    return add_val, subs_val, mult_val, div_val # 여러개의 변수가 한번에 반환되는 것 : packing

a, b, c, d = operator(10, 4) # 반환된 값을 차례대로 특정 변수에 할당하는 것 : unpacking
print( a, b, c, d)

############################## 람다 표현식 ##############################
# 람다표현식이란 ? 특정 기능을 수행하는 함수를 한 줄에 작성 가능
# 함수자체를 또다른 함수의 입력으로 받는 경우, 함수 기능이 간단하거나 일회성일 경우 자주 사용됨
def add(a, b):
    return a+b
print(add(1,3))
print((lambda a, b: a+b)(3,7))

array = [('hong', 50), ('lee', 43), ('kim', 30)]
def my_key(x) :
    return x[1]
print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))

list1 = [1,2,3,4,5]
list2 = [2,3,4,5,6]
resList = map(lambda a, b : a + b, list1, list2)
# map() : 여러개의 리스트 원소에 각각 함수를 적용하고자 할 때 사용

############################## 자주 사용되는 라이브러리 ##############################
# 1. 내장함수 => import 없이 사용 가능
res = sum([1,2,3,4,5]) # 15
min = min(7,4,3,6) # 3
max = max(7,3,4,6) # 7
res2 = eval("(3+5)*7") # 56 => 수식으로 표현된 하나의 식을 수의 형태로 반환
res = sorted([9,1,8,5,4])
reverse_res = sorted([9,1,8,5,4], reverse = True)
# sorted() with key
array = [('hong', 50), ('lee', 43), ('kim', 30)]
result = sorted(array, key=lambda x: x[1], reverse = True)

# 2. itertools: 반복되는 형태의 데이터를 처리하기 위한 기능 제공 => 특히 순열과 조합 라이브러리 완전탐색 문제유형에서 자주사용
# 모든 경우의 수를 고려해야 할 때
# 순열과 조합
# 순열 : nPr = n * (n-1) * ... * (n-r+1)
# 조합 : nCr = n * (n-1) * ... * (n-r+1) / r!
from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']

resultP = list(permutations(data, 3)) # 모든 순열 구하기
resultC = list(combinations(data, 2)) # 2개 뽑는 모든 조합 구하기
resultPr = list(product(data, repeat = 2)) # 2개를 뽑는 모든 순열 구하기 - 중복허용
resultCr = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 - 중복허용
# 3. heapq: 힙(Heap) 자료구조 제공 => 일반적으로 우선순위 큐 기능 구현을 위해 사용
# 4. bisect: 이진탐색기능 제공
# 5. collections: 덱(deque), 카운터(Counter) 등의 유용한 자료구조 포함
# Counter : 등장 횟수를 세는 기능 : 리스트와 같은 반복 가능한(iterable) 객체가 주어졌을 때, 내부의 원소가 몇 번씩 등장했는지 알려줌
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue']) # blue가 등장한 횟수 출력
print(counter['green']) # green이 등장한 횟수 출력
print(dict(counter)) # 사전 자료형으로 반환
 # => {'red' : 2, 'blue':3, 'green':1}
# 6. math: 필수적인 수학적 기능 제공 => 팩토리얼, 제곱근, 최대공약수, 삼각함수 관련 함수부터 파이같은 상수도 포함
import math
def lcm(a, b):
    return a * b // math.gcd(a,b)

a = 21
b = 14
math.gcd(a, b) # 최대 공약수(gcd) 계산
lcm(a, b) # 최소 공배수(lcm) 계산

#######################################################################################################
############################################# 자주쓰이는 함수 ###########################################
#######################################################################################################
# range() 함수
range(a) # 0부터 a-1 까지 정수 범위 반환
range(b, c) # b 부터 c-1 까지 정수 범위 반환
range(d, e, f) # d 부터 e-1까지 f의 간격으로 정수 범위 반환
