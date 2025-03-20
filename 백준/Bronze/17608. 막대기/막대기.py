import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    stack.append(int(input()))

count = 0
max_height = 0 

for i in range(n-1, -1, -1):
    if stack[i] > max_height:  
        count += 1
        max_height = stack[i]  

print(count)