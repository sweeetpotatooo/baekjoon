import sys

n= int(input())
word = []
for i in range(n):
  word.append(input())

word =list(set(word))
word.sort()
word= sorted(word, key=len) 

for i in range(len(word)):
  print(word[i])