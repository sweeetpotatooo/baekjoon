import sys
import heapq

input = sys.stdin.readline

N = int(input())
in_degree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
result = [0] * (N + 1)

# 인접 행렬 입력 받기
for i in range(N):
    row = list(map(int, input().strip()))
    for j, val in enumerate(row):
        if val == 1:
            in_degree[i + 1] += 1     
            graph[j + 1].append(i + 1) 

def topology_sort():
    heap = []
    for node in range(1, N + 1):
        if in_degree[node] == 0:
            heapq.heappush(heap, -node)
    
    order = N
    while heap:
        # 최대 힙-> 음수 -> 원래 값 복원
        current = -heapq.heappop(heap)
        result[current] = order
        order -= 1
        for next_node in graph[current]:
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                heapq.heappush(heap, -next_node)

topology_sort()

if result.count(0) >= 2:
    print(-1)
else:
    print(' '.join(map(str, result[1:])))

