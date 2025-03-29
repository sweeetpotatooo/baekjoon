
import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())  # 순서 수정
    graph[u].append((v, w))              # 올바르게 저장

def dijk(start):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        dist, now = heapq.heappop(heap)
        if dist > distance[now]:
            continue
        for next_city, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_city]:
                distance[next_city] = new_cost
                heapq.heappush(heap, (new_cost, next_city))
    
    return distance

start, end = map(int, input().split())
min_distance = dijk(start)
print(min_distance[end])
