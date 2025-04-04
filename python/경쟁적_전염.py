# 문제
# NxN 크기의 시험관이 있다. 시험관은 1x1 크기의 칸으로 나누어지며, 특정한 위치에는 바이러스가 존재할 수 있다. 
# 모든 바이러스는 1번부터 K번까지의 바이러스 종류 중 하나에 속한다.

# 시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식해 나간다. 
# 단, 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식한다. 
# 또한 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다.

# 시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하시오. 
# 만약 S초가 지난 후에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다. 
# 이 때 X와 Y는 각각 행과 열의 위치를 의미하며, 시험관의 가장 왼쪽 위에 해당하는 곳은 (1,1)에 해당한다.


# 입력
# 첫째 줄에 자연수 N, K가 공백을 기준으로 구분되어 주어진다. (1 ≤ N ≤ 200, 1 ≤ K ≤ 1,000) 둘째 줄부터 N개의 줄에 걸쳐서 시험관의 정보가 주어진다. 
# 각 행은 N개의 원소로 구성되며, 해당 위치에 존재하는 바이러스의 번호가 공백을 기준으로 구분되어 주어진다. 단, 해당 위치에 바이러스가 존재하지 않는 경우 0이 주어진다. 
# 또한 모든 바이러스의 번호는 K이하의 자연수로만 주어진다. N+2번째 줄에는 S, X, Y가 공백을 기준으로 구분되어 주어진다. (0 ≤ S ≤ 10,000, 1 ≤ X, Y ≤ N)

# 출력
# S초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 출력한다. 만약 S초 뒤에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다.
import sys
from collections import deque

def main():
    input = sys.stdin.readline

    # 시험관의 크기(N)와 바이러스 종류의 수(K) 입력
    n, k = map(int, input().split())
    
    graph = []      # 시험관 정보 저장
    viruses = []    # (바이러스 번호, x좌표, y좌표)
    
    # 시험관 정보를 입력받으면서 바이러스 위치 저장
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
        for j in range(n):
            if row[j] != 0:
                viruses.append((row[j], i, j))
    
    # 바이러스 번호가 낮은 순서대로 정렬 (동일 시간에 낮은 번호가 먼저 증식해야 하기 때문)
    viruses.sort(key=lambda x: x[0])
    
    # 큐에 초기 바이러스들 삽입 (시간 정보 0 포함)
    q = deque()
    for virus, x, y in viruses:
        q.append((virus, x, y, 0))
    
    # S초와 (X, Y) 좌표 입력 (좌표는 1-indexed이므로 0-indexed로 변환)
    s, target_x, target_y = map(int, input().split())
    target_x -= 1
    target_y -= 1
    
    # 상, 하, 좌, 우 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # BFS 방식으로 바이러스 전파 (S초까지 진행)
    while q:
        virus, x, y, time = q.popleft()
        
        # S초가 지나면 증식을 멈춤
        if time == s:
            break
        
        # 상하좌우로 바이러스 증식
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 시험관 범위 내이고 아직 바이러스가 없는 경우 증식 진행
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, nx, ny, time + 1))
    
    # S초 후 (X, Y)에 존재하는 바이러스 번호 출력 (없으면 0)
    print(graph[target_x][target_y])

if __name__ == '__main__':
    main()
