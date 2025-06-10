import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
result = []

for _ in range(N):
    board.append(input().strip())  # Added .strip() to remove newline

for i in range(N-7):
    for j in range(M-7):
        idx1 = 0
        idx2 = 0
        for k in range(i, i+8):
            for h in range(j, j+8):
                if (k + h) % 2 == 0:
                    if board[k][h] != 'W':  # Fixed: was board[i][j]
                        idx1 += 1
                    if board[k][h] != 'B':  # Fixed: was board[i][j]
                        idx2 += 1
                else:
                    if board[k][h] != 'B':  # Fixed: was board[i][j]
                        idx1 += 1
                    if board[k][h] != 'W':  # Fixed: was board[i][j]
                        idx2 += 1
        result.append(min(idx1, idx2))  # Moved inside the outer loops

print(min(result))