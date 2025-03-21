import sys

def cal(s):
    stack = []
    answer = 0
    tmp = 1

    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
            tmp *= 2
        elif s[i] == '[':
            stack.append('[')
            tmp *= 3
        elif s[i] == ')':
            if not stack or stack[-1] != '(':
                return 0
            if s[i-1] == '(':
                answer += tmp
            stack.pop()
            tmp //= 2
        elif s[i] == ']':
            if not stack or stack[-1] != '[':
                return 0
            if s[i-1] == '[':
                answer += tmp
            stack.pop()
            tmp //= 3

    if stack:
        return 0
    return answer

# 입력받기
s = input().strip()
print(cal(s))
