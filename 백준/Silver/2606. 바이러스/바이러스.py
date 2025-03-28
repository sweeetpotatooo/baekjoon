import sys
input = sys.stdin.readline

n_computer = int(input())
link = int(input())

graph = {i: [] for i in range(1, n_computer + 1)}

for _ in range(link):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = set()


def dfs(v):
    visited.add(v)
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(neighbor)

dfs(1)

print(len(visited) - 1)

