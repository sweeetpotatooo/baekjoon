import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())

if N >= K:
    print(N - K)
else:
    visited = [False] * 100001
    queue = deque([(N, 0)])
    visited[N] = True
    
    while queue:
        pos, time = queue.popleft()
        if pos == K:
            print(time)
            break
        for next_pos in (pos - 1, pos + 1, pos * 2):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))