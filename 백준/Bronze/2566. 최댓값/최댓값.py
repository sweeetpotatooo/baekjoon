import sys
input = sys.stdin.readline
matrix = []
for _ in range(9):
  row = list(map(int,input().split()))
  matrix.append(row)

max_value = 0
row = 0
col = 0

for i in range(9):
    for j in range(9):
        if matrix[i][j] >= max_value:
            max_value = matrix[i][j]
            row = i+1
            col = j+1

print(max_value)
print(row, col)