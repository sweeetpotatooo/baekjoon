import sys
input = sys.stdin.readline

L, P = map(int, input().split())
part_list = list(map(int, input().split()))

result = [x - (L * P) for x in part_list]
print(*result)
