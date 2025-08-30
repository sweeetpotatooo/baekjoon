import sys
input = sys.stdin.readline
n = int(input())
a, b = 0, 1
for _ in range(n):
    a, b = b, a + b
print(a)