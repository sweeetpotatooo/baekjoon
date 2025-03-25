
import sys
import heapq
input = sys.stdin.readline

min_heap = []

n= int(input())
for i in range(n):
  x = int(input())
  if x==0:
    if min_heap:
      print(heapq.heappop(min_heap))
    else:
      print(0)
  else:
        heapq.heappush(min_heap,x)