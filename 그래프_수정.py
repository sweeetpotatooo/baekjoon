# 문제
# N개의 정점이 있는 그래프가 주어지면, 다음과 같은 방법에 의해서 정점의 번호를 다시 매기고 싶다.
# 모든 그래프의 번호는 1보다 크거나 같고 N보다 작거나 같은 번호를 가져야 한다.
# 만약 V1에서 V2로 연결된 간선이 있다면, V2의 번호는 V1보다 커야 한다.
# 위와 같은 조건을 이용해서 그래프의 번호를 다시 매긴 후에, 1번 정점의 새로 고친 번호를 M1, 2번 정점의 새로 고친 번호를 M2, ..., 
# N번 정점의 새로 고친 번호를 MN이라고 하면, N개의 수열이 만들어진다.
# 이 수열을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N이 주어진다. 둘째 줄부터 N개의 줄에는 인접행렬 형식으로 입력이 주어진다. 
# 0은 연결되지 않았음을 의미하고, 1은 연결되었다는 것을 의미한다. N은 50보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 수열의 각 원소를 차례대로 공백을 사이에 두고 출력한다. 만약 그래프의 번호를 수정할 수 없다면 -1을 출력한다. 
# 답이 여러 개일 경우에는 사전 순으로 제일 앞서는 것을 출력한다.

import sys
import heapq

input = sys.stdin.readline

N = int(input())
in_degree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
result = [0] * (N + 1)

# 인접 행렬 입력 받기
for i in range(N):
    row = list(map(int, input().strip()))
    for j, val in enumerate(row):
        if val == 1:
            in_degree[i + 1] += 1     
            graph[j + 1].append(i + 1) 

def topology_sort():
    heap = []
    for node in range(1, N + 1):
        if in_degree[node] == 0:
            heapq.heappush(heap, -node)
    
    order = N
    while heap:
        # 최대 힙-> 음수 -> 원래 값 복원
        current = -heapq.heappop(heap)
        result[current] = order
        order -= 1
        for next_node in graph[current]:
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                heapq.heappush(heap, -next_node)

topology_sort()

if result.count(0) >= 2:
    print(-1)
else:
    print(' '.join(map(str, result[1:])))

