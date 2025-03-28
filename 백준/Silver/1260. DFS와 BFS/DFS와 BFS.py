
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for k in graph:
    graph[k].sort()


dfs_result = []
visited_dfs = set()
def dfs(v):
    visited_dfs.add(v)
    dfs_result.append(v)
    for neighbor in graph[v]:
        if neighbor not in visited_dfs:
            dfs(neighbor)
dfs(v)

def bfs(v):
    visited_bfs = set([v])
    bfs_result = []
    queue = [v]
    while queue:
        cur = queue.pop(0)
        bfs_result.append(cur)
        for neighbor in graph[cur]:
            if neighbor not in visited_bfs:
                visited_bfs.add(neighbor)
                queue.append(neighbor)
    return bfs_result
bfs_result = bfs(v)

print(*dfs_result)
print(*bfs_result)