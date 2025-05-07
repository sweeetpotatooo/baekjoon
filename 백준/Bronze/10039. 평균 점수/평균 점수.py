
import sys
input = sys.stdin.readline
score = []
for i in range(5):
  n = int(input())
  if (n > 40):
    score.append(n)
  else:
    score.append(40)

print(sum(score)//5)