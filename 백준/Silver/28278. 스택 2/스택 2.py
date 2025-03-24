
import sys
input = sys.stdin.readline

N = int(input())
stack= []
for i in range (N):
  num = input().split()
  if num[0] == '1':
    stack.append(num[1])
  elif num[0] == '2':
    if stack:
      pop = stack.pop()
      print(pop)
    else:
      print(-1)
  elif num[0] == '3':
    print(len(stack))
  elif num[0] == '4':
    if stack:
      print(0)
    else:
      print(1)
  else:
    if stack:
      print(stack[-1])
    else:
      print(-1)


