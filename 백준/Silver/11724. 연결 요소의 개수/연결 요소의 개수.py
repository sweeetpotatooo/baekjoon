import sys
input = sys.stdin.readline

n,m = map(int,input().split())

graph = {i: [] for i in range(1,n+1)}

for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = set()
components = 0

def dfs(v):
    visited.add(v)
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(neighbor)

for node in range(1, n+1):
    if node not in visited:
        dfs(node)
        components += 1

print(components)