
import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    min_heap = []      
    max_heap = []      
    valid = [False] * k  

    for i in range(k):
        op, num = input().split()
        num = int(num)
        if op == "I":
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            valid[i] = True
        else:
            if num == 1: 
                while max_heap and not valid[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    valid[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            elif num == -1:  
                while min_heap and not valid[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    valid[min_heap[0][1]] = False
                    heapq.heappop(min_heap)


    while min_heap and not valid[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not valid[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        sys.stdout.write("EMPTY\n")
    else:
        max_val = -max_heap[0][0]
        min_val = min_heap[0][0]
        sys.stdout.write(f"{max_val} {min_val}\n")
