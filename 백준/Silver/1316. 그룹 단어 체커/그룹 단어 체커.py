import sys
input = sys.stdin.readline
N = int(input())
count = 0
for _ in range(N):
    word = input().rstrip()
    stack = []
    for i in range(len(word)):
        if not stack:
            stack.append(word[i])
        elif stack[-1] != word[i]:
            stack.append(word[i])
    if len(stack) == len(set(stack)):
        count += 1
print(count)