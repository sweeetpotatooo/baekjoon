# 문제
# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.
# 입력
# 첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

# 둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

# 출력
# check 연산이 주어질때마다, 결과를 출력한다.
import sys
input = sys.stdin.readline
write = sys.stdout.write

S = set()
M = int(input())

for _ in range(M):
    cmd = input().strip().split()
    
    if cmd[0] == "add":
        S.add(int(cmd[1]))
    elif cmd[0] == "remove":
        S.discard(int(cmd[1]))
    elif cmd[0] == "check":
        write('1\n' if int(cmd[1]) in S else '0\n')
    elif cmd[0] == "toggle":
        x = int(cmd[1])
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif cmd[0] == "all":
        S = set(range(1, 21))
    elif cmd[0] == "empty":
        S.clear()
