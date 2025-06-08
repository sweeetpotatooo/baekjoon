N = int(input())
num = 666
count = 0

while True:
  if '666' in str(num):
    count+=1
    if count == N:
      break
  
  num += 1 

print(num)