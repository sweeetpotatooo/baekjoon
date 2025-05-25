import sys
input = sys.stdin.readline

N = int(input())
p = list(map(int, input().split()))
p.sort()

total = 0
current_sum = 0

for time in p:
    current_sum += time
    total += current_sum

print(total)