import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
longest = [0] * (n + 1)
prev_nodes = [[] for _ in range(n + 1)]

# 그래프 구성
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    indegree[b] += 1

start, end = map(int, input().split())

# 위상 정렬을 통한 최장 경로 계산 및 이전 노드 기록
queue = deque([start])
while queue:
    cur = queue.popleft()
    for nxt, cost in graph[cur]:
        if longest[nxt] < longest[cur] + cost:
            longest[nxt] = longest[cur] + cost
            prev_nodes[nxt] = [cur]
        elif longest[nxt] == longest[cur] + cost:
            prev_nodes[nxt].append(cur)
        
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)

print(longest[end])  
# start에서 end까지의 최장 시간 출력

# 역추적하여 임계 경로 상의 간선 수 계산
visited = [False] * (n + 1)
queue = deque([end])
count = 0

while queue:
    cur = queue.popleft()
    for prev in prev_nodes[cur]:
        count += 1
        if not visited[prev]:
            visited[prev] = True
            queue.append(prev)

print(count)