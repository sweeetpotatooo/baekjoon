import sys
import numpy as np
from itertools import permutations

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

# numpy 배열로 변환
A = np.array(A)

# 1. 차이 행렬 M (N x N)
#    A[:, np.newaxis] : 세로벡터, A[np.newaxis, :] : 가로벡터
#    이 둘의 차이의 절댓값을 구하면 NxN 행렬이 됨
M = np.abs(A[:, np.newaxis] - A[np.newaxis, :])

max_value = 0

# 2. 모든 순열을 확인
for perm in permutations(range(N)):
    # M[perm[k], perm[k+1]] 로 쉽게 차이 조회
    total = 0
    for k in range(N-1):
        total += M[perm[k], perm[k+1]]
    max_value = max(max_value, total)

print(int(max_value))
