# 문제
# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. 
# <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

# 출력
# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.


import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)] # 0: 집 없음, 1: 집 있음
visited = [[False] * N for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
count = 0 # 단지 수
result = [] # 단지내 세대수 리스트, 결과적으로 한줄에 result하나씩 출력 

def bfs(x, y): # bfs로 size 리턴 
    queue = deque([(x, y)])
    visited[x][y] = True
    size = 1 # 단지내 세대수 

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                size += 1
    return size

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            count += 1
            result.append(bfs(i, j))

result.sort()
print(count)

for i in result:
    print(i)

# 큐가 빌때까지 인접한 집 찾기, not visited-> 방문처리후 큐에 추가
# 연결된 집의 개수 size 에 누적 후 반환
# 집 있으면서 not visited--> 단지 탐색
# 단지 찾을때마다 count 증가, result에 추가
# result 정렬 
