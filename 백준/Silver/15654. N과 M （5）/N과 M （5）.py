import sys
from itertools import permutations
input = sys.stdin.readline
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
for perm in permutations(numbers, m):
    print(' '.join(map(str, perm)))
  