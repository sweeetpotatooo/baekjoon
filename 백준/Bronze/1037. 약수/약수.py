import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
print(min(data) * max(data))