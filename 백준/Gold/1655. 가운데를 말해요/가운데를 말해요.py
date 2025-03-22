
import sys
import heapq

input = sys.stdin.readline

min_heap = []
max_heap = []


def push_num(num):
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)


    if min_heap and -max_heap[0] > min_heap[0]:
        temp_min = heapq.heappop(min_heap)
        temp_max = heapq.heappop(max_heap)
        heapq.heappush(max_heap, -temp_min)
        heapq.heappush(min_heap, -temp_max)


def find_median():
    if len(min_heap) == len(max_heap):
        return min(min_heap[0], -max_heap[0])
    else:
        return -max_heap[0]


n = int(input())

for _ in range(n):
    num = int(input())
    push_num(num)
    print(find_median())
