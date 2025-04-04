import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  coins = list(map(int,input().split()))
  goal = int(input())

  dp = [0]* (goal+1)
  dp[0] = 1
  for coin in coins:
    for money in range(goal+1):
      if money>=coin:
        dp[money] += dp[money-coin] 
  print(dp[goal])