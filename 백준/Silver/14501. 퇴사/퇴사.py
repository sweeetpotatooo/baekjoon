import sys
input = sys.stdin.readline
n = int(input())
time = [0] * n
price = [0] * n
for i in range(n):
    t, p = map(int, input().split())
    time[i] = t
    price[i] = p
dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    if i + time[i] <= n:
        dp[i] = max(dp[i + 1], dp[i + time[i]] + price[i])
    else:
        dp[i] = dp[i + 1]
print(dp[0])