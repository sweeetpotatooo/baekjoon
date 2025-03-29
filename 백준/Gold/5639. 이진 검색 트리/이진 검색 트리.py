import sys
sys.setrecursionlimit(10**6)
input_data = sys.stdin.read().split()
pre = list(map(int, input_data))
n = len(pre)
result = []
idx = 0

def rec(lower, upper):
    global idx
    if idx >= n:
        return
    # 현재 노드가 허용 범위에 없다면 재귀 종료
    if pre[idx] < lower or pre[idx] > upper:
        return

    root = pre[idx]
    idx += 1
    # 왼쪽 서브트리: 허용 범위는 (lower, root)
    rec(lower, root)
    # 오른쪽 서브트리: 허용 범위는 (root, upper)
    rec(root, upper)
    result.append(root)

# 초기 허용 범위는 음의 무한대 ~ 양의 무한대로 설정
rec(float('-inf'), float('inf'))
sys.stdout.write("\n".join(map(str, result)))
