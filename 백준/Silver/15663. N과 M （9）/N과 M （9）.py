import sys
input = sys.stdin.readline

def backtrack(path, used):
    if len(path) == m:
        result.add(tuple(path))
        return
    for i in range(n):
        if not used[i]:
            used[i] = True
            backtrack(path + [numbers[i]], used)
            used[i] = False

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
result = set()
backtrack([], [False]*n)
for seq in sorted(result):
    print(' '.join(map(str, seq)))
