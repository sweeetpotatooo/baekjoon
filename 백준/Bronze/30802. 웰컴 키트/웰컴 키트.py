import math

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

# 티셔츠 묶음 수 계산
tshirt_bundles = 0
for size in sizes:
    tshirt_bundles += math.ceil(size / T)

# 펜 묶음 수와 한 자루씩 주문하는 개수 계산
pen_bundles = N // P
pen_singles = N % P

print(tshirt_bundles)
print(pen_bundles, pen_singles)
