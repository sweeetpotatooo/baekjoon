# 문제
# NxN 크기의 시험관이 있다. 시험관은 1x1 크기의 칸으로 나누어지며, 특정한 위치에는 바이러스가 존재할 수 있다. 
# 모든 바이러스는 1번부터 K번까지의 바이러스 종류 중 하나에 속한다.

# 시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식해 나간다. 
# 단, 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식한다. 
# 또한 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다.

# 시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하시오. 
# 만약 S초가 지난 후에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다. 
# 이 때 X와 Y는 각각 행과 열의 위치를 의미하며, 시험관의 가장 왼쪽 위에 해당하는 곳은 (1,1)에 해당한다.


# 입력
# 첫째 줄에 자연수 N, K가 공백을 기준으로 구분되어 주어진다. (1 ≤ N ≤ 200, 1 ≤ K ≤ 1,000) 둘째 줄부터 N개의 줄에 걸쳐서 시험관의 정보가 주어진다. 
# 각 행은 N개의 원소로 구성되며, 해당 위치에 존재하는 바이러스의 번호가 공백을 기준으로 구분되어 주어진다. 단, 해당 위치에 바이러스가 존재하지 않는 경우 0이 주어진다. 
# 또한 모든 바이러스의 번호는 K이하의 자연수로만 주어진다. N+2번째 줄에는 S, X, Y가 공백을 기준으로 구분되어 주어진다. (0 ≤ S ≤ 10,000, 1 ≤ X, Y ≤ N)

# 출력
# S초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 출력한다. 만약 S초 뒤에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다.

import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
virus = [] #(바이러스 번호, x좌표, y좌표, 시간), 바이러스 번호 작은순 minheap
graph = []


for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            heapq.heappush(virus, (graph[i][j], i, j, 0))

s, x, y = map(int, input().split())

x -= 1
y -= 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while virus:
    v, a, b, t = heapq.heappop(virus)
    if t == s:
        break
    for i in range(4):
        nx, ny = a + dx[i], b + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = v
            heapq.heappush(virus, (v, nx, ny, t + 1))

if graph[x][y] == 0:
    print(0)
else:
    print(graph[x][y])


# 상하좌우로 이동 가능한 칸을 계산, 비어 있으면 바이러스를 증식. 증식된 바이러스 heapq에 추가
# t == s 조건을 통해 s초까지만 증식을 진행.
