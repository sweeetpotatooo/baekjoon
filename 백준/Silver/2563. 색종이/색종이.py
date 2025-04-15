import sys
input = sys.stdin.readline

paper = [[0] *100 for _ in range(100)]
paper_n = int(input())

for _ in range(paper_n):
  x,y = map(int,input().split())
  for i in range(x, x+10):
    for j in range(y, y+10):
      paper[i][j] =1

area =0
for row in paper:
  area +=sum(row)

print(area)