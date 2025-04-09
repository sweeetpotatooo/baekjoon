import sys
input = sys.stdin.readline

N = int(input())

crane = list(map(int, input().split()))
crane.sort(reverse=True)

M = int(input())

box = list(map(int, input().split()))
box.sort(reverse=True)

count = 0
if box[0]>crane[0]:count = -1
else:
    while box:
      for i in crane:
        if box and i < box[-1]:
          continue
        for j in box:
          if i >= j:
            box.remove(j)
            break
      count+=1

print(count)