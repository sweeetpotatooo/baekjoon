N, M = map(int, input().split())
baskets = list(range(1, N + 1))

for _ in range(M):
    i, j = map(int, input().split())
    # i-1부터 j까지를 슬라이싱해서 역순으로 바꿈
    baskets[i-1:j] = baskets[i-1:j][::-1]

print(*baskets)
