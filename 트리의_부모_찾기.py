# 문제
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

# 출력
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

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