import sys
input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    left = []
    right = []
    cmd = input().rstrip('\n')
    
    for char in cmd:
        if char == '<':
            if left:
                right.append(left.pop())
        elif char == '>':
            if right:
                left.append(right.pop())
        elif char == '-':
            if left:
                left.pop()
        else:
            left.append(char)
    
    left.extend(reversed(right))
    
    print(''.join(left))
