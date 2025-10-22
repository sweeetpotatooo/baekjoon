import sys
input = sys.stdin.readline
K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]
left, right = 1, max(lines)
result = 0
while left <= right:
    mid = (left + right) // 2
    count = 0
    for line in lines:
        count += line // mid
    if count >= N:
        result = mid
        left = mid + 1
    else:
        right = mid - 1
print(result)