import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, color):
    colors[node] = color
    for neighbor in graph[node]:
        if colors[neighbor] == 0:
            if not dfs(neighbor, -color):
                return False
        elif colors[neighbor] == color:
            return False
    return True

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        u, w = map(int, input().split())
        graph[u].append(w)
        graph[w].append(u)
    
    colors = [0] * (v + 1)
    bipartite = True
    for i in range(1, v + 1):
        if colors[i] == 0:
            if not dfs(i, 1):
                bipartite = False
                break
    print("YES" if bipartite else "NO")
