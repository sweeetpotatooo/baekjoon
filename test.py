import sys
input = sys.stdin.readline
# :받은_편지함_트레이: 입력
V, E = map(int, input().split())
edges = []
for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
# :아래쪽_화살표: 간선을 비용 기준으로 정렬
edges.sort()
# :시계_반대_방향_화살표: 부모 초기화
parent = [i for i in range(V + 1)]
# :렌치: 유니온 파인드용 함수들
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])  # 경로 압축
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
# :흰색_확인_표시: 크루스칼 핵심
result = 0
for cost, a, b in edges:
    # 사이클이 아니면 MST에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)