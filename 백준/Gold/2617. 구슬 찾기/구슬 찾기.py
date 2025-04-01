import sys
input = sys.stdin.readline

n,m =  map(int, input().split())

heavy_list = [[] for _ in range(n+1)] 
light_list = [[] for _ in range(n+1)]

for _ in range(m):
    heavy, light = map(int, input().split())
    heavy_list[heavy].append(light)
    light_list[light].append(heavy)

def dfs(list, root):
    count = 0
    for node in list[root]:
        if not visited[node]:
            visited[node] = True
            count += 1 + dfs(list, node)
    return count


mid = (n+1)/2
result = 0

for root in range(1, n+1):
    visited = [False] * (n+1)
    if dfs(heavy_list, root) >= mid:
        result += 1
    if dfs(light_list, root) >= mid:
        result += 1

print(result)