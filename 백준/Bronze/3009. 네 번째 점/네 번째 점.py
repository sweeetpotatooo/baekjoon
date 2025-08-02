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