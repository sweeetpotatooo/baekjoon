import sys
input = sys.stdin.readline

N = int(input())
  
Sum = 0

for i in range (N):
    Sum = Sum + i + 1

print(Sum)
print(Sum**2) 

Sum = 0
for i in range (N):
    Sum = Sum + (i + 1)**3
print(Sum)