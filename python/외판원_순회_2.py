import sys

input = sys.stdin.readline

N = int(input())  # 도시 수
fee = [list(map(int, input().split())) for _ in range(N)]
min_fee = float('inf')  # 숫자형 무한대 사용

def dfs_backtracking(start, cur, cost, visited):
    global min_fee

    if len(visited) == N:  # 모든 도시를 방문한 경우
        if fee[cur][start] != 0:
            min_fee = min(min_fee, cost + fee[cur][start])
        return

    for i in range(N):  # 모든 도시 탐색
        if fee[cur][i] != 0 and i not in visited and cost + fee[cur][i] < min_fee:
            dfs_backtracking(start, i, cost + fee[cur][i], visited | {i})

# 각 도시를 출발점으로 DFS 실행
for i in range(N):
    dfs_backtracking(i, i, 0, {i})

print(min_fee)
