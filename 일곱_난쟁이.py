height=[]
for i in range(9):
  height.append(int(input()))
height.sort()

height_sum=sum(height)
for i in range(9):
  for j in range(i+1,9):
    if height_sum- height[i]-height[j] ==100:
      del height[j]
      del height[i]
      break
  if len(height) ==7:
     break
for h in height:  
  print(h)

