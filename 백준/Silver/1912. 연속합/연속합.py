import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

current_max = arr[0]
max_sum = arr[0]
for i in range(1, n):
    current_max = max(arr[i], current_max + arr[i])
    if current_max > max_sum:
        max_sum = current_max

print(max_sum)