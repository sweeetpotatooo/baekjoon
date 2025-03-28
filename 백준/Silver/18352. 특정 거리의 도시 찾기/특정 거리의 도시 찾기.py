
import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = {}
for i in range(n+1):
    graph[i] = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0


que = deque([x])
while que:
    v = que.popleft()
    for nv in graph[v]:
        if distance[nv] == -1:
            distance[nv] = distance[v] + 1
            que.append(nv)

found = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        found = True
if not found:
    print(-1)


