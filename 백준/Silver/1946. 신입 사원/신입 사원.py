import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  score = []
  for _ in range(N):
    document, interview = map(int, input().split())
    score.append([document, interview])
  score.sort()
  top = 0
  result = 1

  for i in range(1,len(score)):
    if score[i][1] < score[top][1]:
      top = i
      result += 1
  print(result)
