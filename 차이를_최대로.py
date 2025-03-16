import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

# 1. 차이 행렬 M 구성 (NxN)
M = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        M[i][j] = abs(A[i] - A[j])

max_value = 0

for perm in permutations(range(N)):
    total = 0
    for k in range(N-1):
        total += M[perm[k]][perm[k+1]]
    max_value = max(max_value, total)

print(max_value)
