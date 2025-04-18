# 문제
# 우리는 어떤 장난감을 여러 가지 부품으로 조립하여 만들려고 한다. 
# 이 장난감을 만드는데는 기본 부품과 그 기본 부품으로 조립하여 만든 중간 부품이 사용된다. 
# 기본 부품은 다른 부품을 사용하여 조립될 수 없는 부품이다. 중간 부품은 또 다른 중간 부품이나 기본 부품을 이용하여 만들어지는 부품이다.

# 예를 들어보자. 기본 부품으로서 1, 2, 3, 4가 있다. 
# 중간 부품 5는 2개의 기본 부품 1과 2개의 기본 부품 2로 만들어진다. 
# 그리고 중간 부품 6은 2개의 중간 부품 5, 3개의 기본 부품 3과 4개의 기본 부품 4로 만들어진다. 
# 마지막으로 장난감 완제품 7은 2개의 중간 부품 5, 3개의 중간 부품 6과 5개의 기본 부품 4로 만들어진다. 
# 이런 경우에 장난감 완제품 7을 만드는데 필요한 기본 부품의 개수는 1번 16개, 2번 16개, 3번 9개, 4번 17개이다.

# 이와 같이 어떤 장난감 완제품과 그에 필요한 부품들 사이의 관계가 주어져 있을 때 하나의 장난감 완제품을 조립하기 위하여 필요한 기본 부품의 종류별 개수를 계산하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 자연수 N(3 ≤ N ≤ 100)이 주어지는데, 1부터 N-1까지는 기본 부품이나 중간 부품의 번호를 나타내고, N은 완제품의 번호를 나타낸다. 
# 그리고 그 다음 줄에는 자연수 M(3 ≤ M ≤ 100)이 주어지고, 그 다음 M개의 줄에는 어떤 부품을 완성하는데 필요한 부품들 간의 관계가 3개의 자연수 X, Y, K로 주어진다. 
# 이 뜻은 "중간 부품이나 완제품 X를 만드는데 중간 부품 혹은 기본 부품 Y가 K개 필요하다"는 뜻이다. 두 중간 부품이 서로를 필요로 하는 경우가 없다.

# 출력
# 하나의 완제품을 조립하는데 필요한 기본 부품의 수를 한 줄에 하나씩 출력하되(중간 부품은 출력하지 않음), 반드시 기본 부품의 번호가 작은 것부터 큰 순서가 되도록 한다. 
# 각 줄에는 기본 부품의 번호와 소요 개수를 출력한다.

# 정답은 2,147,483,647 이하이다.

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
queue = deque()
indegree=[0]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[b].append((a, c))
    indegree[a] += 1


def topological_sort():
    result = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
            result[i][i] = 1

    while queue:
        node = queue.popleft()
        for next_node, cost in graph[node]:
            for i in range(1, n+1):
                result[next_node][i] += result[node][i] * cost
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)
    return result

result_f = topological_sort()
for i in range(1, n):
    if result_f[n][i] != 0:
        print(i, result_f[n][i])



# import sys
# from collections import deque
# input = sys.stdin.readline

# # 노드(부품) 개수와 간선(조립 관계) 개수 입력
# n = int(input())
# m = int(input())

# # 각 노드의 후속 노드를 저장할 인접 리스트 초기화
# graph = [[] for _ in range(n+1)]
# # 위상 정렬에 사용할 큐 초기화
# queue = deque()
# # 각 노드의 진입 차수를 저장할 리스트 초기화
# indegree = [0] * (n+1)

# # m개의 조립 관계 입력 받기
# # 각 줄은 a, b, c로 구성
# # "b번 부품을 조립할 때 a번 부품이 c개 필요하다"는 의미로 해석 가능
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     # b에서 a로 연결되는 간선 저장 (a는 b의 구성 부품)
#     graph[b].append((a, c))
#     # a의 진입 차수 증가 (a를 조립하기 위해 b가 선행되어야 함)
#     indegree[a] += 1

# def topological_sort():
#     # 결과 행렬: result[x][y]는 x번 부품을 만들 때 기본 부품 y가 몇 개 필요한지를 의미
#     result = [[0] * (n+1) for _ in range(n+1)]

#     # 진입 차수가 0인 노드는 기본 부품임
#     for i in range(1, n+1):
#         if indegree[i] == 0:
#             queue.append(i)
#             # 기본 부품의 경우 자기 자신을 1개 가진다고 초기화
#             result[i][i] = 1

#     # 위상 정렬을 진행하며 각 부품별 기본 부품의 개수를 누적
#     while queue:
#         # 큐에서 현재 노드(부품) 꺼내기
#         node = queue.popleft()
#         # 현재 노드에 연결된 후속 노드(조립 부품)들에 대해 처리
#         for next_node, cost in graph[node]:
#             # 모든 기본 부품에 대해 현재 노드가 next_node에 기여하는 양 계산
#             for i in range(1, n+1):
#                 result[next_node][i] += result[node][i] * cost
#             # 후속 노드의 진입 차수를 감소
#             indegree[next_node] -= 1
#             # 진입 차수가 0이 되면 큐에 추가 (조립이 가능한 상태)
#             if indegree[next_node] == 0:
#                 queue.append(next_node)
#     return result

# # 위상 정렬 수행 및 결과 행렬 획득
# result_f = topological_sort()

# # 최종 제품(n번 부품)에 대해 기본 부품들만 결과 출력
# # result_f[n][i]가 0이 아니면 i번 기본 부품이 필요하다는 의미
# for i in range(1, n):
#     if result_f[n][i] != 0:
#         print(i, result_f[n][i])
