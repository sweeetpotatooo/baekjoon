import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v, e = map(int, input().split())

edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

parent = []
for i in range(v+1):
    parent.append(i)
    

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_b] = root_a
        return True
    return False

result = 0 

for c, a, b in edges:
    if union(a, b):
        result += c

print(result)
