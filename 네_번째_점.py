# 문제
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

# 입력
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

# 출력
# 직사각형의 네 번째 점의 좌표를 출력한다.

import sys
input = sys.stdin.readline
points = [tuple(map(int, input().split())) for _ in range(3)]
x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]
x = 0
y = 0
for i in range(3):
    if x_coords.count(x_coords[i]) == 1:
        x = x_coords[i]
    if y_coords.count(y_coords[i]) == 1:
        y = y_coords[i]
print(x, y)