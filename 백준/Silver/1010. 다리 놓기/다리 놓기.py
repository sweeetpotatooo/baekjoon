import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # 초기값 설정
    for i in range(M + 1):
        dp[0][i] = 1
    
    # DP 테이블 채우기
    for i in range(1, N + 1):
        for j in range(i, M + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
    print(dp[N][M])