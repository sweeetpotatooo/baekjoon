import sys
input= sys.stdin.readline

n=int(input())

count = 0

while n % 5 != 0:
  n-=2
  count+=1

  if n < 0:
    print(-1)
    exit(0)

print(count+ n//5)