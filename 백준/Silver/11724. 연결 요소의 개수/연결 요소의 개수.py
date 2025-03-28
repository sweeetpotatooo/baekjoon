import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    xroot = find(x)
    yroot = find(y)
    if xroot != yroot:
        parent[yroot] = xroot

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

distinct_roots = []
for i in range(1, n+1):
    root = find(i)
    if root not in distinct_roots:
        distinct_roots.append(root)
components = len(distinct_roots)
print(components)