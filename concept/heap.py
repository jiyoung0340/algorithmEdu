# 힙 정렬
import sys
import heapq # 기본으로 제공되는 heap은 MinHeap임!
input = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []

    for value in iterable: # 모든 원소를 차례대로 힙에 삽입
        heapq.heappush(h, value) # MaxHeap의 경우 value를 -value로
    for i in range(len(h)): # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
        result.append(heapq.heappop(h)) # MaxHeap의 경우 pop()한 후, -붙이기
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

res = heapsort(arr)

for i in range(n):
    print(res[i])