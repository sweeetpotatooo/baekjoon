
import sys
input = sys.stdin.readline

alphabet = [0]*26

word = input().strip()

for i in word:
    alphabet[ord(i)-97] += 1

print(*alphabet)