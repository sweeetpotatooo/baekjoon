import sys
input = sys.stdin.readline
N, M = map(int, input().split())
result = []
def backtracking():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N + 1):
        result.append(i)
        backtracking()
        result.pop()
backtracking()
