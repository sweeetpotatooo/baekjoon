# 문제
# N개의 강의가 있다. 우리는 모든 강의의 시작하는 시간과 끝나는 시간을 알고 있다. 
# 이때, 우리는 최대한 적은 수의 강의실을 사용하여 모든 강의가 이루어지게 하고 싶다.

# 물론, 한 강의실에서는 동시에 2개 이상의 강의를 진행할 수 없고, 한 강의의 종료시간과 다른 강의의 시작시간이 겹치는 것은 상관없다. 
# 필요한 최소 강의실 수 K와, 각 강의마다 강의실을 배정하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 강의의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에 걸쳐 각 줄마다 세 개의 정수가 주어지는데, 순서대로 강의 번호, 강의 시작 시간, 강의 종료 시간을 의미한다. 
# 강의 번호는 1부터 N까지 붙어 있으며, 입력에서 꼭 순서대로 주어지지 않을 수 있으나 한 번씩만 주어진다. 강의 시작 시간과 강의 종료 시간은 0 이상 10억 이하의 정수이고, 시작 시간은 종료 시간보다 작다.

# 출력
# 첫째 줄에 필요한 최소 강의실 개수 K를 출력한다. 둘째 줄부터 N개의 줄에 걸쳐 각 강의에 배정할 강의실 번호를 순서대로 출력한다. 편의상 강의실 번호는 1, 2, ..., K 로 매긴다.
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

# 이거 회의실 배정이랑 비슷한거 같은데 그때는 그 뭐냐 키값 람다로 끝나는 시간 시작시간으로 설정
# 강의 끝나는 시간 순 정렬
# 2순위 시작 시간 순으로 정렬

