import sys
input = sys.stdin.readline
for _ in range(3):
    a = sum(map(int, input().split()))
    print('D' if a == 0 else 'C' if a == 1 else 'B' if a == 2 else 'A' if a == 3 else 'E')
    