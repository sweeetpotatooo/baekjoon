import sys
input = sys.stdin.readline

line_count = 0
MAX_LINES = 100

while line_count < MAX_LINES:
    try:
        line = input().rstrip()
        if not line:  # EOF 처리
            break
        print(line)
        line_count += 1
    except EOFError:
        break