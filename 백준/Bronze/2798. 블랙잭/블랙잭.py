import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

best = 0
# i < j < k 조합으로 3장 선택
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            s = cards[i] + cards[j] + cards[k]
            if s <= M and s > best:
                best = s
                # M에 딱 맞으면 더 볼 필요 없음
                if best == M:
                    print(best)
                    sys.exit(0)

print(best)

