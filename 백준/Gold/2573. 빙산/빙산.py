
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x, y, visited):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0<=nx<n and 0<=ny<m and grid[nx][ny]>0 and not visited[nx][ny]:
                visited[nx][ny]=True
                queue.append((nx,ny))

def melt():
    temp = [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if grid[x][y]>0:
                cnt=0
                for d in range(4):
                    nx, ny = x+dx[d], y+dy[d]
                    if 0<=nx<n and 0<=ny<m and grid[nx][ny]==0:
                        cnt+=1
                temp[x][y]=max(grid[x][y]-cnt, 0)
    return temp

year = 0
while True:
    visited = [[False]*m for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j]>0 and not visited[i][j]:
                bfs(i,j,visited)
                cnt += 1

    if cnt==0: 
        print(0)
        break
    if cnt>=2:
        print(year)
        break

    grid = melt()
    year += 1
