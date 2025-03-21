import sys
input = sys.stdin.readline

n, k = map(int, input().split())
number = input().strip()

stack = []

for i in range(n):
    while k > 0 and stack and stack[-1] < number[i]:
        stack.pop()
        k -= 1
    stack.append(number[i])

result = stack[:-k] if k else stack

print(''.join(result))
