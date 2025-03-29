
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n= int(input())
graph = {i: [] for i in range(1, n + 1)}


for _ in range(n-1):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

parent = [0] * (n+1)

def dfs(start, end):
  for neighbor in graph[start]:
    if neighbor!= end:
      parent[neighbor] = start
      dfs(neighbor, start)

dfs(1,0)

for i in range(2, n + 1):
    print(parent[i])