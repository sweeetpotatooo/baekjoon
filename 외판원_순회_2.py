import sys

input = sys.stdin.readline

N = int(input())  # 도시수
fee = [list(map(int, input().split())) for _ in range(N)]
min_fee = int(1,000,000)  # 최소 비용

def dfs_backtracking(start, next, price, visited):
    global min_fee

    if len(visited) == N:  # 모든 도시를 방문
        if fee[next][start] != 0:
            min_fee = min(min_fee, price + fee[next][start])
        return

    for i in range(N):  # 모든 도시 탐색
        if fee[next][i] != 0 and i not in visited and price + fee[next][i] < min_fee:
            dfs_backtracking(start, i, price + fee[next][i], visited | {i})  # 방문한 도시 추가


# 각 도시를 출발점으로 설정
for i in range(N):
    dfs_backtracking(i, i, 0, {i})  # 출발 도시를 집합으로 전달

print(min_fee)
