import sys
input = sys.stdin.readline

n = int(input())
mat = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for l in range(1, n):
    for i in range(n - l):
        j = i + l
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + mat[i][0] * mat[k][1] * mat[j][1]
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][n-1])
