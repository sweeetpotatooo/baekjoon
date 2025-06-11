import sys
input = sys.stdin.readline
while True:
    line = input().rstrip()
    if line == '#':
        break
    count = sum(1 for char in line if char.lower() in 'aeiou')
    print(count)