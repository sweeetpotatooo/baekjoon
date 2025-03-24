
import sys
input = sys.stdin.readline

while True:
    sentence = input().rstrip('\n')
    if sentence == ".":
        break

    sentence_list = list(sentence)
    stack = []
    is_balanced = True

    for char in sentence_list:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                is_balanced = False
                break
            else:
                stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                is_balanced = False
                break
            else:
                stack.pop()
    
    if is_balanced and not stack:
        print("yes")
    else:
        print("no")
