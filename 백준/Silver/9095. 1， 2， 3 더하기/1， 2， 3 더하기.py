import sys
input= sys.stdin.readline

def sum123(n):
  if n==1:
    return 1
  elif n==2:
    return 2 
  elif n==3:
    return 4
  else:
    return sum123(n-1)+sum123(n-2)+sum123(n-3)
  
  

T= int(input())
for i in range(T):
  n=int(input())
  print(sum123(n))