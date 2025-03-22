import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    h, o = map(int, input().split())
    if h > o:
        h, o = o, h
    q.append((h, o))
d = int(input())

q.sort(key = lambda x : (x[1], x[0]))

lines = []
max_count = 0
for h, o in q:
    end = o
    start = end - d
    
    heapq.heappush(lines, h)
    
    while lines and lines[0] < start:
        heapq.heappop(lines)
    
    max_count = max(max_count, len(lines))

print(max_count)