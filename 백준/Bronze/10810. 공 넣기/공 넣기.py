import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
basket = [0] * (N + 1) 
for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i, j + 1):
        basket[x] = k
print(*basket[1:])