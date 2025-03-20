n = int(input())
stack = []
count = 1

for _ in range(n):
    num = int(input())
    stack.append(num)

peek = stack[-1]

for _ in range(n - 1):
    stack.pop()
    if stack and peek < stack[-1]:  
        count += 1

print(count)
