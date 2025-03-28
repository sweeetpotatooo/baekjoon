
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph:
    graph[key].sort()

def dfs_stack(start):
    visited = set()
    result = []
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    return result

def bfs(start):
    visited = set([start])
    result = []
    queue = [start]
    while queue:
        cur = queue.pop(0)
        result.append(cur)
        for neighbor in graph[cur]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

dfs_result = dfs_stack(v)
bfs_result = bfs(v)

print(*dfs_result)
print(*bfs_result)
