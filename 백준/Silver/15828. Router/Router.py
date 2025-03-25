
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()

while True:
  info = int(input())
  if info == -1:
    break
  elif info == 0:
    queue.popleft()
  elif len(queue)<n:
    queue.append(info)
if queue:
  print(' '.join(map(str, queue)))
else:
  print("empty")
  