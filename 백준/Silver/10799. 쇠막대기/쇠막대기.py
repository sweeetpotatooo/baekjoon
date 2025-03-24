import sys
input = sys.stdin.readline

bracket = input().strip()  
stack = []
count = 0

for i, char in enumerate(bracket):
    if char == "(":
        stack.append(char)
    else: 
        if i > 0 and bracket[i-1] == "(":
            stack.pop()  
            count += len(stack)  
        else:
            stack.pop()
            count += 1

print(count)