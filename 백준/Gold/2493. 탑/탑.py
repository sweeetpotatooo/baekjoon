n = int(input())
towers = list(map(int, input().split()))
stack = []
stack.append((int(1e9), 0))

result = []
for i in range(1, n+1):
    while stack[-1][0] <= towers[i-1]:
        stack.pop()
    result.append(stack[-1][1])
    stack.append((towers[i-1], i))

print(*result)