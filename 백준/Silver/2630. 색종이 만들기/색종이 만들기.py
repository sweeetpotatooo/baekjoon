import sys
input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)] 
white ,blue = 0,0

def cut(x, y, n):
   global white , blue
   color = paper[x][y]# 첫번째 색
   for i in range(x,x+n):# x로 나누기
       for j in range(y,y+n):# y로 나누기
         if color != paper[i][j]: # 첫번째 색이랑 달라지면 자른다
            #여기서 재귀 해야됨
            cut(x, y, n//2)
            cut(x, y+n//2, n//2)
            cut(x+n//2, y, n//2)
            cut(x+n//2, y+n//2, n//2)
            return
   if color == 1:
      blue+=1
   else:
      white+=1

cut(0,0,n)


print(white)
print(blue)