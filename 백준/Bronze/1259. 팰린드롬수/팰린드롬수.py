import sys
input = sys.stdin.readline

while True:
    word = input().strip()
    if word == '0':  
        break
    reverse = ''.join(reversed(word))  
    if reverse == word:
        print("yes")
    else:
        print("no")
