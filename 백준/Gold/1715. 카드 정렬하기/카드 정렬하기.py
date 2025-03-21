import sys
import heapq
input = sys.stdin.readline

n= int(input())
num_card = []
for i in range(n):
    heapq.heappush(num_card,int(input()))

total = 0
while len(num_card) > 1:
    a = heapq.heappop(num_card)
    b = heapq.heappop(num_card)
    sum_card = a+b

    total += sum_card
    heapq.heappush(num_card, sum_card)

print(total)


