import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
grid = [list(input().strip()) for _ in range(r)]

water_time = [[-1] * c for _ in range(r)]
hedgehog_time = [[-1] * c for _ in range(r)]

water_q = deque()
hedgehog_q = deque()

for i in range(r):
    for j in range(c):
        if grid[i][j] == '*':
            water_q.append((i, j))
            water_time[i][j] = 0
        elif grid[i][j] == 'S':
            hedgehog_q.append((i, j))
            hedgehog_time[i][j] = 0

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while water_q:
    x, y = water_q.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            if water_time[nx][ny] == -1 and grid[nx][ny] == '.':
                water_time[nx][ny] = water_time[x][y] + 1
                water_q.append((nx, ny))

while hedgehog_q:
    x, y = hedgehog_q.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            if hedgehog_time[nx][ny] != -1:
                continue
            if grid[nx][ny] == 'D':
                print(hedgehog_time[x][y] + 1)
                sys.exit(0)
            if grid[nx][ny] == '.':
                if water_time[nx][ny] != -1 and water_time[nx][ny] <= hedgehog_time[x][y] + 1:
                    continue
                hedgehog_time[nx][ny] = hedgehog_time[x][y] + 1
                hedgehog_q.append((nx, ny))

print("KAKTUS")
