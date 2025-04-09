import sys
input = sys.stdin.readline

word = input().rstrip()
word = word.upper()
count = [0] * 26
for i in word:
    count[ord(i) - ord('A')] += 1
max_count = max(count)
max_index = []
for i in range(26):
    if count[i] == max_count:
        max_index.append(i)
if len(max_index) > 1:
    print('?')
else:
    print(chr(max_index[0] + ord('A')))