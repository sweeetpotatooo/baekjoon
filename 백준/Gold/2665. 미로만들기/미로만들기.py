import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
rooms = []
n = int(input())
for i in range(n):
    rooms.append(list(map(int, input().strip())))

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited = [[-1] * n for _ in range(n)]
    visited[0][0] = 0
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == n - 1:
            return visited[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if rooms[nx][ny] == 1:
                    queue.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    return -1

print(bfs())
