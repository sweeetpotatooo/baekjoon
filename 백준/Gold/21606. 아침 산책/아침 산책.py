import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(v,count):
  visited[v] = True

  for i in graph[v]:
    if location[i] == 1:
      count+=1
    elif not visited[i] and location[i] ==0:
      count = dfs(i,count)
  return count
ans = 0

n = int(input())
location = [0]+list(map(int, input().strip())) # 0이면 실외 1이면 실내, 인덱스 1부터 시작하려고
graph = [[] for _ in range(n + 1)]

for i in range(n-1):
  u,v = map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)
  if location[u] ==1 and location[v] ==1:
    ans+=2

sum = 0
visited = [False] *(n+1)
for i in range(1,n+1):
    if not visited[i] and location[i] ==0:
      x = dfs(i,0)
      sum+= x*(x-1)
print(sum +ans)

