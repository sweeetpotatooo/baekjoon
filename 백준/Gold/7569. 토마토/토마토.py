import sys
from collections import deque
input = sys.stdin.readline

M,N,H = map(int, input().split())
box = []
for _ in range(H):
    box.append([list(map(int, input().split())) for _ in range(N)])
visited = [[[0]*M for _ in range(N)] for _ in range(H)]
queue = deque()
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                queue.append((i, j, k))
                visited[i][j][k] = 1
            elif box[i][j][k] == -1:
                visited[i][j][k] = -1
days = 0
while queue:
    for _ in range(len(queue)):
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and box[nx][ny][nz] == 0 and visited[nx][ny][nz] == 0:
                queue.append((nx, ny, nz))
                visited[nx][ny][nz] = 1
    days += 1


all_ripe = True
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0 and visited[i][j][k] == 0:
                all_ripe = False
if all_ripe:
    print(days - 1)
else:
    print(-1)
