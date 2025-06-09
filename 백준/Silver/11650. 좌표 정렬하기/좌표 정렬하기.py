N = int(input())
locate = []
for i in range(N):
  x, y = map(int,input().split())
  locate.append([x,y])
locate.sort(key = lambda x: (x[0], x[1]))
for i in locate:
  print(i[0], i[1])