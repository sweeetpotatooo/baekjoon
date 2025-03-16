import sys 
input = sys.stdin.readline
def solve_n_queens(n, row=0, cols=set(), diag1=set(), diag2=set()):
    if row == n:
        return 1

    count = 0
    for col in range(n):
        # 현재 열, 주 대각선(row - col), 부 대각선(row + col)이 사용 중이면 건너뜁니다.
        if col in cols or (row - col) in diag1 or (row + col) in diag2:
            continue

        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)

        count += solve_n_queens(n, row + 1, cols, diag1, diag2)

        cols.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)

    return count

num_queen = int(input())
print(solve_n_queens(num_queen))
