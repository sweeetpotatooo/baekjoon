import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

maze = []
for i in range(n):
    line = input().strip()
    row = []
    for ch in line:
        row.append(int(ch))
    maze.append(row)

queue = deque()
queue.append((0, 0))

while queue:
    x, y = queue.popleft()
    
    if x == n - 1 and y == m - 1:
        print(maze[x][y])
        break
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            queue.append((nx, ny))
