import sys
input = sys.stdin.readline
n = int(input())
files = [input().rstrip() for _ in range(n)]
pattern = list(files[0])
for file in files[1:]:
    for i in range(len(file)):
        if pattern[i] != file[i]:
            pattern[i] = '?'
print(''.join(pattern))