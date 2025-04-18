# 한수
def digit (x):
  return list(map(int, str(x)))

n= int(input())
count= 0

if n<100:
  print (n)
else:
  for i in range(100,n+1):
    digit_n=digit(i)
    if digit_n[0]+digit_n[2] == digit_n[1]*2:
      count+=1

  print(count+99)