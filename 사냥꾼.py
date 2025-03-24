# 문제
# KOI 사냥터에는 N 마리의 동물들이 각각 특정한 위치에 살고 있다. 사냥터에 온 사냥꾼은 일직선 상에 위치한 M 개의 사대(총을 쏘는 장소)에서만 사격이 가능하다. 
# 편의상, 일직선을 x-축이라 가정하고, 사대의 위치 x1, x2, ..., xM은 x-좌표 값이라고 하자. 
# 각 동물이 사는 위치는 (a1, b1), (a2, b2), ..., (aN, bN)과 같이 x,y-좌표 값으로 표시하자. 
# 동물의 위치를 나타내는 모든 좌표 값은 양의 정수이다.

# 사냥꾼이 가지고 있는 총의 사정거리가 L이라고 하면, 사냥꾼은 한 사대에서 거리가 L 보다 작거나 같은 위치의 동물들을 잡을 수 있다고 한다. 
# 단, 사대의 위치 xi와 동물의 위치 (aj, bj) 간의 거리는 |xi-aj| + bj로 계산한다.

# 예를 들어, 아래의 그림과 같은 사냥터를 생각해 보자. (사대는 작은 사각형으로, 동물의 위치는 작은 원으로 표시되어 있다.) 
# 사정거리 L이 4라고 하면, 점선으로 표시된 영역은 왼쪽에서 세 번째 사대에서 사냥이 가능한 영역이다.

# 사대의 위치와 동물들의 위치가 주어졌을 때, 잡을 수 있는 동물의 수를 출력하는 프로그램을 작성하시오.

# 입력
# 입력의 첫 줄에는 사대의 수 M (1 ≤ M ≤ 100,000), 동물의 수 N (1 ≤ N ≤ 100,000), 사정거리 L (1 ≤ L ≤ 1,000,000,000)이 빈칸을 사이에 두고 주어진다. 
# 두 번째 줄에는 사대의 위치를 나타내는 M개의 x-좌표 값이 빈칸을 사이에 두고 양의 정수로 주어진다. 
# 이후 N개의 각 줄에는 각 동물의 사는 위치를 나타내는 좌표 값이 x-좌표 값, y-좌표 값의 순서로 빈칸을 사이에 두고 양의 정수로 주어진다. 
# 사대의 위치가 겹치는 경우는 없으며, 동물들의 위치가 겹치는 경우도 없다. 모든 좌표 값은 1,000,000,000보다 작거나 같은 양의 정수이다.

# 출력
# 출력은 단 한 줄이며, 잡을 수 있는 동물의 수를 음수가 아닌 정수로 출력한다.


#Brute_force
# import sys
# input = sys.stdin.readline

# M, N, L = map(int,input().split())
# sadae = list(map(int, input().split()))
# animals = []
# count = 0

# for _ in range(N):
#     row = list(map(int, input().split()))
#     animals.append(row)


# for i in range(M):
#     j = len(animals) - 1
#     while j >= 0:
#         if abs(sadae[i] - animals[j][0]) + animals[j][1] <= L:
#             count += 1
#             del animals[j]
#         j -= 1
# print(count)

# binary search

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
