import sys, heapq
input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
lecture = [0 for _ in range(n+1)]
arr.sort(key=lambda x: (x[1], x[2]))
room = []
for i in range(1, n+1):
    heapq.heappush(room, i)

minHeap = []
for x in arr:
    while minHeap and minHeap[0][0] <= x[1]:
        end, r = heapq.heappop(minHeap)
        heapq.heappush(room, r)

    r = heapq.heappop(room)
    heapq.heappush(minHeap, [x[2], r])
    lecture[x[0]] = r

print(max(lecture))
for x in lecture[1:]:
    print(x)