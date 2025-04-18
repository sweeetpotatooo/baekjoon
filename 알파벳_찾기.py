s= list(input())
alphabet = list("abcdefghijklmnopqrstuvwxyz")
for i in alphabet:
  if i in s:
    print(s.index(i), end=" ")
  else:
    print(-1, end=" ")