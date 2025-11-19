# 문제
# "두리"라는 나라가 있다. 이 나라에서 사용되는 동전은 1원, 2원, 4원, 8원, 16원, 32원, 64원, 128원, 256원, 512원짜리 이렇게 총 10가지이다. 이 나라의 국민인 아리는 10가지의 동전을 각각 1개씩 총 10개를 가지고 있다.

# 아리는 샌드위치를 사러 빵집에 가기로 했다. 그런데 빵집에 잔돈이 없어서 샌드위치 가격 S 을 정확하게 지불하지 않으면 샌드위치를 살 수 없다고 한다. 아리가 가지고 있는 동전들을 가지고 계산을 하던 도중 아리의 친구인 쿠기가 마침 빵집에 들어왔다. 쿠기는 10종류의 동전 중에 모든 종류가 아니라 일부 종류의 동전을 각각 1개씩 가지고 있다. 쿠기가 가지고 있는 동전들의 총 금액은 M 원이다. 쿠기는 아리에게 자신이 가진 돈 중에 일부 또는 전체를 흔쾌히 빌려줄 수 있다고 한다. 단, 아리는 양심 상 자신의 돈을 남긴 상태로 쿠기에게 돈을 빌릴 수는 없어서 자신이 가진 돈을 모두 사용한 후에 부족한 금액에 대해서 쿠기에게 돈을 빌리려고 한다.

# 아리는 상황에 따라 쿠기에게 인사를 다르게 하려고 한다. 아리는 과연 쿠기에게 뭐라고 할지 구해보자!

# 입력
# 첫 번째 줄에 공백을 기준으로 샌드위치 가격 S(1 ≤ S ≤ 2048)와 쿠기가 가지고 있는 금액 M(1 ≤ M ≤ 1023)이 주어진다.

# 출력
# 아리의 돈으로만 살 수 있다면 "No thanks"를 출력하고, 쿠기의 도움을 받아야만 살 수 있다면 "Thanks" 그리고 쿠기가 돈을 빌려주더라도 샌드위치를 살 수 없다면 "Impossible"를 출력한다.

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
