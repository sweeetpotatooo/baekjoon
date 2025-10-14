import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())
for seq in combinations(range(1, N + 1), M):
    print(*seq)