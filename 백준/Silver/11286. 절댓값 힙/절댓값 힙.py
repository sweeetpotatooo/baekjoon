
import sys
import heapq

input = sys.stdin.readline
n = int(input().strip())
min_heap = []

for _ in range(n):
    x = int(input().strip())
    if x == 0:
        if min_heap:
            abs_x, val = heapq.heappop(min_heap)
            print(val)
        else:
            print(0)
    else:
        heapq.heappush(min_heap, (abs(x), x))
