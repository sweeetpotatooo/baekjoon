
import sys
input = sys.stdin.readline

sentence = input().strip()
bomb = input().strip()
stack = []

for ch in sentence:
    stack.append(ch)
    if len(stack) >= len(bomb):
      last_part = ''.join(stack[-len(bomb):])
      if last_part == bomb:
          for _ in range(len(bomb)):
            stack.pop()

result = ''.join(stack)
if result:
    print(result)
else:
    print("FRULA")