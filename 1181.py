import sys
# 단어정렬
n= int(input())
word = []
for i in range(n):
  word.append(sys.stdin.readline())
sorted_words= sorted(word, key=len)

for i in range(len(sorted_words)):
  print(sorted_words[i])