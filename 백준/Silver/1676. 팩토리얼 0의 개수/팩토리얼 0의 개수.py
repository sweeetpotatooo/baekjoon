import sys
input = sys.stdin.readline
N = int(input())
count = 0
while N >= 5:
    N //= 5
    count += N
print(count)