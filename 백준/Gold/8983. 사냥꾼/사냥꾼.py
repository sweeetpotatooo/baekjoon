
import sys
input = sys.stdin.readline
from bisect import bisect_left

M, N, L = map(int, input().split())
sadae = list(map(int, input().split()))
sadae.sort()  # 사대 위치 정렬
count = 0

for _ in range(N):
    x, y = map(int, input().split())
    # 동물의 x 좌표에 가장 가까운 사대를 찾는다
    idx = bisect_left(sadae, x)

    # 현재 인덱스 또는 그 이전 인덱스 사대 중에서 가장 가까운 것을 선택
    near = []
    if idx < M:
        near.append(abs(sadae[idx] - x) + y)
    if idx > 0:
        near.append(abs(sadae[idx - 1] - x) + y)

    # 가까운 사대로부터 사정거리 이내면 count 증가
    if any(dist <= L for dist in near):
        count += 1

print(count)
