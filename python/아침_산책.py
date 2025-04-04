# 문제
# 아침 산책을 즐기는 서현이는 서울과학고에 입학해서도 아침 산책을 즐기려고 합니다. 서현이는 산책을 위해 서울과학고의 지리를 분석했고, 그 결과 서울과학고를 
# $N$개의 장소를 
# $N-1$개의 길이 잇는 트리 형태로 단순화시킬 수 있었습니다. 트리 구조이므로, 모든 장소를 몇 개의 길을 통해 오고갈 수 있습니다.

# 아침 산책은 시작점과 도착점을 정하고, 시작점에서 도착점까지 트리 위의 단순 경로(같은 점을 여러 번 지나지 않는 경로)를 따라 걷게 됩니다. 
# 트리 위의 두 점 사이의 경로는 유일하므로 시작점과 도착점이 정해지면 경로는 유일하게 결정됩니다.

# $N$개 장소 중에 일부 장소는 실내이며, 나머지 장소는 실외입니다. 
# 서현이는 산책을 시작하기 전부터 운동을 하는 것을 원치 않기 때문에, 산책의 시작점과 끝점은 모두 실내여야 합니다. 
# 또한, 산책 도중에 실내 장소를 만나면 산책을 그만두고자 하는 욕구가 생기기 때문에, 산책 경로 위에 시작점과 끝점을 제외하고 실내 장소가 있으면 안 됩니다.

# 서현이는 매일 다른 산책 경로를 걷고자 합니다. 서로 다른 산책 경로가 몇 가지 있는지 구해 봅시다.

# 입력
# 첫 줄에는 정점의 수 
# $N$이 주어집니다.

# 둘째 줄에는 1과 0으로 이루어진 길이 
# $N$의 문자열 
# $A$가 주어집니다. 
# $i$번째 문자 
# $A_i$가 1일 경우 
# $i$번 장소는 실내이며, 0인 경우 
# $i$번 장소는 실외입니다.

# 셋째 줄부터 
# $N+1$번 줄까지는 
# $i+2$번 줄에 트리의 각 간선을 나타내는 두 정수 
# $u_i$, 
# $v_i$가 주어집니다. 이는 
# $i$번째 간선이 
# $u_i$번 정점과 
# $v_i$번 정점을 연결한다는 의미입니다.

# 출력
# 가능한 서로 다른 산책 경로의 수를 출력합니다.

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

