# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.



# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 
# 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. 
# w와 h는 50보다 작거나 같은 양의 정수이다.

# 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

# 입력의 마지막 줄에는 0이 두 개 주어진다.

# 출력
# 각 테스트 케이스에 대해서, 섬의 개수를 출력한다.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
def dfs(x, y):
    visited[y][x] = True
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h:
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                dfs(nx, ny)
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    count = 0
    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1 and not visited[y][x]:
                dfs(x, y)
                count += 1
    print(count)
    