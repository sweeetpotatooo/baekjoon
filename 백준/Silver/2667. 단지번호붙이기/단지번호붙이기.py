
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
