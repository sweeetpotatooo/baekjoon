import sys
input = sys.stdin.readline
k = int(input())
stack = []
for _ in range(k):
  n = int(input())
  if n != 0:
    stack.append(n)
  else:
    if stack: 
        stack.pop()
print(sum(stack))