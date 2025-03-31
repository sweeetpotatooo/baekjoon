
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
queue = deque()
indegree=[0]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[b].append((a, c))
    indegree[a] += 1


def topological_sort():
    result = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
            result[i][i] = 1

    while queue:
        node = queue.popleft()
        for next_node, cost in graph[node]:
            for i in range(1, n+1):
                result[next_node][i] += result[node][i] * cost
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)
    return result

result_f = topological_sort()
for i in range(1, n):
    if result_f[n][i] != 0:
        print(i, result_f[n][i])