import sys
input = sys.stdin.readline

N, M = map(int, input().split())

not_heard = set()
not_saw = set()

for _ in range(N):
    not_heard.add(input().strip())

for _ in range(M):
    not_saw.add(input().strip())

result = not_heard & not_saw
sorted_result = sorted(result)

print(len(result))
for name in sorted_result:
    print(name)