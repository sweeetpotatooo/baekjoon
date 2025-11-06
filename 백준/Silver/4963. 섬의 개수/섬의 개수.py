import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
def dfs(x, y):
    visited[y][x] = True
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h:
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                dfs(nx, ny)
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    count = 0
    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1 and not visited[y][x]:
                dfs(x, y)
                count += 1
    print(count)
    