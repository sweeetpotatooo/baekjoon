
import sys
from collections import deque
input = sys.stdin.readline


T = int(input().strip())
for i in range(T):
  N,M = map(int,input().split())
  grade = list(map(int,input().split()))

  queue = deque((p, idx) for idx, p in enumerate(grade))
    
  print_count = 0  
    
  while queue:
        current = queue[0]
        if any(current[0] < q[0] for q in queue):
            queue.rotate(-1)
        else:

            printed = queue.popleft()
            print_count += 1
            if printed[1] == M:
                print(print_count)
                break
