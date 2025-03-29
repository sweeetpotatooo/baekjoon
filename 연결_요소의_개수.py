# 문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.
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




#union-find
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# parent = [0] * (n+1)
# for i in range(n+1):
#     parent[i] = i

# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]

# def union(x, y):
#     xroot = find(x)
#     yroot = find(y)
#     if xroot != yroot:
#         parent[yroot] = xroot

# for _ in range(m):
#     a, b = map(int, input().split())
#     union(a, b)

# distinct_roots = []
# for i in range(1, n+1):
#     root = find(i)
#     if root not in distinct_roots:
#         distinct_roots.append(root)
# components = len(distinct_roots)
# print(components)