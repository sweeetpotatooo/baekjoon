x= int(input().split())
y= int(input().split())
w= int(input().split())
h= int(input().split())

print(min(x,y,w-x,h-y))