import sys
input = sys.stdin.readline
N = int(input())
original = N  
count = 0
while True:
    count += 1
    s = f"{N:02d}"         
    sum_digits = int(s[0]) + int(s[1])
    N = int(s[1] + str(sum_digits % 10))
    if N == original:
        break
print(count)