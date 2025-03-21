import sys
from collections import deque
input = sys.stdin.readline


n, k = map(int,input().split())

yosepus = []
queue = deque()

for i in range(1, n + 1):
    queue.append(i)

while queue:
    for i in range(k - 1):
        queue.append(queue.popleft())
    yosepus.append(queue.popleft()) 

print("<", end="")
print(", ".join(map(str, yosepus)), end="")
print(">")