
import sys
import heapq
input = sys.stdin.readline
N = int(input())
dasom = int(input())
vote = []

for _ in range(N - 1):
    num = int(input())
    heapq.heappush(vote, (-num, num))

cnt = 0
while vote:
    num = heapq.heappop(vote)[1]
    if num >= dasom:
        num -= 1
        dasom += 1
        cnt += 1
        heapq.heappush(vote, (-num, num))

print(cnt)