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
