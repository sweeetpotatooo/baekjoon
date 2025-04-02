# 문제
# n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그
# 러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.

# 입력
# 첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 
# 동전의 가치는 100,000보다 작거나 같은 자연수이다. 가치가 같은 동전이 여러 번 주어질 수도 있다.

# 출력
# 첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.



from collections import deque

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# 중복 제거 (동전 중복값이 있을 수 있으므로)
coins = list(set(coins))

visited = [False] * (k + 1)
queue = deque()
queue.append((0, 0))  # (현재금액, 사용동전수)
visited[0] = True

while queue:
    current, count = queue.popleft()

    for coin in coins:
        next_value = current + coin
        if next_value == k:
            print(count + 1)
            exit()
        if next_value < k and not visited[next_value]:
            visited[next_value] = True
            queue.append((next_value, count + 1))

print(-1)


# #DP
# import sys
# input = sys.stdin.readline
# n, k = map(int, input().split())
# coins = []
# for _ in range(n):
#     coins.append(int(input()))
# coins.sort(reverse=True)
# dp = [float('inf')] * (k + 1)
# dp[0] = 0
# for coin in coins:
#     for i in range(coin, k + 1):
#         dp[i] = min(dp[i], dp[i - coin] + 1)
# if dp[k] == float('inf'):
#     print(-1)
# else:
#     print(dp[k])
