
import sys
from collections import deque
input = sys.stdin.readline
q = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                q.append((i, j))
                arr[i][j] = 0
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                            arr[nx][ny] = 0
                            q.append((nx, ny))
    
    print(cnt)