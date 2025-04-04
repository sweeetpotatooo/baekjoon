n=int(input())
for i in range(n):
  count, word = input().split()
  for j in word:
    print(j*int(count), end='')
  print()