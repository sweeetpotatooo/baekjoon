import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
nums = [a, b, c]
nums_sorted = sorted(nums)
print(nums_sorted[1])
