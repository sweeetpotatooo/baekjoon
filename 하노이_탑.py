def hanoi(num_c, start, goal):
  if num_c ==1:
    print(start, goal) 
    return 
  hanoi(num_c-1, start, 6-start-goal)
  print(start, goal)
  hanoi(num_c -1, 6-start-goal, goal)


n = int(input())
print(2**n-1)
if n<=20:
  hanoi(n,1,3)