
import sys
input = sys.stdin.readline
chess_pieces = [1, 1, 2, 2, 2, 8]
pieces = list(map(int, input().split()))
result = []
for i in range(len(chess_pieces)):
    result.append(chess_pieces[i] - pieces[i])
print(*result)