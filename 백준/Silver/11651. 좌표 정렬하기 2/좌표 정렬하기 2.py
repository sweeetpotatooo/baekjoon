import sys
input = sys.stdin.readline
N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((y, x))  # (y좌표, x좌표)로 저장
points.sort()  # y좌표 기준으로 정렬, y좌표가 같으면 x좌표 기준으로 정렬
for y, x in points:
    print(x, y)  # x좌표, y좌표 순으로 출력