import sys
input = sys.stdin.readline

M, N, L = map(int,input().split())
sadae = list(map(int, input().split()))
animals = []
count = 0

for _ in range(N):
    row = list(map(int, input().split()))
    animals.append(row)


for i in range(M):
    j = len(animals) - 1
    while j >= 0:
        if abs(sadae[i] - animals[j][0]) + animals[j][1] <= L:
            count += 1
            del animals[j]
        j -= 1
print(count)