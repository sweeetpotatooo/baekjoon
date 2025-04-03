import sys
input = sys.stdin.readline
N, M = map(int, input().split())

floor = [input().strip() for _ in range(N)]
visited = [[False] * M for _ in range(N)]
count = 0

for i in range(N):
    for j in range(M):
        if floor[i][j] == '-' and not visited[i][j]:
            count += 1
            for k in range(j, M):
                if floor[i][k] == '-':
                    visited[i][k] = True
                else:
                    break
        elif floor[i][j] == '|' and not visited[i][j]:
            count += 1
            for k in range(i, N):
                if floor[k][j] == '|':
                    visited[k][j] = True
                else:
                    break
print(count)