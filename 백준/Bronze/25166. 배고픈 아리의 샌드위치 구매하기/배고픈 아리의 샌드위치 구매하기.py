import sys
input = sys.stdin.readline
S, M = map(int, input().split())
ari_coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
ari_total = sum(ari_coins)

if S > ari_total + M:
    print("Impossible")
    exit()


def can_make_with_ari(target):
    dp = [False] * (target + 1)
    dp[0] = True
    for coin in ari_coins:
        for i in range(target, coin - 1, -1):
            if dp[i - coin]:
                dp[i] = True
    return dp[target]

if can_make_with_ari(S):
    print("No thanks")
    exit()


need = S - ari_total
if need <= 0:
    print("No thanks")
    exit()


kuki_coins = []
tmp = M
for v in reversed(ari_coins):
    if tmp >= v:
        kuki_coins.append(v)
        tmp -= v

possible = [False] * (M + 1)
possible[0] = True
for coin in kuki_coins:
    for i in range(M, coin - 1, -1):
        if possible[i - coin]:
            possible[i] = True
if need <= M and possible[need]:
    print("Thanks")
else:
    print("Impossible")
