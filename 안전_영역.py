import sys
from collections import deque

N = int(sys.stdin.readline())
water = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def iterative_dfs(x, y, h, visited):
    stack = [(x, y)]
    visited[x * N + y] = True
    while stack:
        cx, cy = stack.pop()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                nidx = nx * N + ny
                if not visited[nidx] and water[nx][ny] > h:
                    visited[nidx] = True
                    stack.append((nx, ny))

ans = 0
unique_heights = sorted(set([0] + [val for row in water for val in row]))

for h in unique_heights:
    visited = [False] * (N * N)
    count = 0
    for i in range(N):
        for j in range(N):
            if water[i][j] > h and not visited[i * N + j]:
                iterative_dfs(i, j, h, visited)
                count += 1
    ans = max(ans, count)

print(ans)
