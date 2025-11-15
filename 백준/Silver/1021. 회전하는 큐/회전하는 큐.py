import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
targets = list(map(int, input().split()))
queue = deque(range(1, n + 1))
total_operations = 0
for target in targets:
    idx = queue.index(target)
    if idx <= len(queue) // 2:
        queue.rotate(-idx)
        total_operations += idx
    else:
        queue.rotate(len(queue) - idx)
        total_operations += len(queue) - idx
    queue.popleft()
print(total_operations)