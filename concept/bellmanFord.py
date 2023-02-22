# 벨만 포드 알고리즘 : O(VE)
# 음수 간선이 포함된 상황의 최단거리 문제
# ex. 타임머신
# N개의 도시가 있고 한 도시~다른 도시인 버스가 M개 있다. 각 버스는 A(시작도시), B(도착도시), C(이동하는데 걸리는 시간)으로 나타낼 수 있다.
# 단, C는 양수가 아닐 수도 있다. C가 0인 경우는 순간 이동을 한 경우, 음수일 경우는 타임머신으로 시간을 되돌아 가는 경우이다.
# 이때 1번 도시에서 출발해 나머지 도시로 가는 가장 빠른 시간을 구하라.
# N : 1 <= N <= 500
# M : 1 <= M <= 6000
#
# 1. 출발 노드 설정
# 2. 최단 거리 테이블 초기화
# 3. 다음 과정을 N - 1번 반복
#     1) 전체 간선 E개를 하나씩 확인
#     2) 각 간선을 거쳐 다른 노드로 가는 비용을 계산해 최단 거리 테이블 갱신
# 만약 음수 간선 순환이 발생하는지 체크하고 싶다면 3번의 과정을 한번 더 수행해 최단 거리 테이블이 갱신된다면
# 음수 간선 순환이 존재하는 것.

import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    dist[start] = 0 # 시작 노드 초기화
    for i in range(n): # 전체 n번의 라운드 반복
        for j in range(m): # 매 반복마다 "모든 간선"을 확인하며
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost: # 현재간선을 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
                dist[next_node] = dist[cur] + cost
                if i == n - 1: # n번째 라운드에서도 값이 갱신된다면 음수 순환 존재
                    return True
    return False

n, m = map(int, input().split()) # n:노드의 개수, m:간선의 개수
edges = [] # 모든 간선에 대한 정보를 담는 리스트
dist = [INF] * (n + 1) # 최단 거리 테이블 무한으로 초기화

for _ in range(m): # 모든 간선 정보를 입력받기
    a, b, c = map(int, input().split())
    edges.append((a, b, c)) # a번 노드에서 b번 노드로 가는 비용이 c라는 의미

# 벨만 포드 알고리즘 수행
negative_cycle = bf(1) # 1번 노드가 시작 노드

if negative_cycle:
    print("-1")
else:
    for i in range(2, n + 1): # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
        if dist[i] == INF : # 도달할 수 없는 경우, -1 출력
            print("-1")
        else: # 도달할 수 있는 경우 거리 출력
            print(dist[i])