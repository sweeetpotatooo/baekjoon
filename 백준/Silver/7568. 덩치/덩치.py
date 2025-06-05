import sys
input = sys.stdin.readline

N = int(input().strip())

frame = []
for _ in range(N):
    weight, height = map(int, input().split())
    frame.append((weight, height))

ranks = []
for i in frame:
    rank = 1
    for j in frame:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    ranks.append(rank)

print(' '.join(map(str, ranks)))