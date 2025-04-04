import sys
input = sys.stdin.readline

math = input().split("-")
num = []

for i in math:
  sum =0
  plus = i.split('+')
  for j in plus:
    sum+= int(j)
  num.append(sum)

n= num[0]

for i  in range(1,len(num)):
  n-= num[i]
print(n)