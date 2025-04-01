
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
