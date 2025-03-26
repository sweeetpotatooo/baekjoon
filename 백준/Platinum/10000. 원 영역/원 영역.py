import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
MX = int(1e9)+1

class CircleNode:
    def __init__(self, st, en):
        self.st = st                # 원의 시작점
        self.en = en                # 원의 끝점
        self.dia = en - st          # 원의 지름 
        self.children = []          # 자식 원 목록

def append_circle(node):
    global IDX
    while IDX < n and circles[IDX][1] <= node.en:
        child = CircleNode(circles[IDX][0], circles[IDX][1])
        node.children.append(child)
        IDX += 1
        append_circle(child)

def cal_area(node):
    global COUNT
    COUNT += 1
    children_diameter_sum = 0
    for child in node.children:
        children_diameter_sum += child.dia
        cal_area(child)
    if children_diameter_sum == node.dia:
        COUNT += 1
       
n = int(input())
circles = []
for _ in range(n):
    x, r = map(int, input().split())
    circles.append((x - r, x + r))
circles.sort(key = lambda x : (x[0], -x[1]))

root = CircleNode(-MX, MX)
IDX, COUNT = 0, 0
append_circle(root)
cal_area(root)

print(COUNT)