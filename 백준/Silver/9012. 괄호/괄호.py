import sys
input = sys.stdin.readline

def is_vps(s):
    s = s.strip()  # 불필요한 공백 제거
    # 문자열 길이가 홀수이면 VPS가 될 수 없음
    if len(s) % 2 != 0:
        print('NO')
        return
    
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:  # c가 ')'인 경우
            if not stack:
                print('NO')
                return
            stack.pop()
    # 모든 괄호를 처리한 후 스택이 비어있어야 올바른 괄호 문자열
    if stack:
        print('NO')
    else:
        print('YES')

t = int(input())
for _ in range(t):
    ps = input()
    is_vps(ps)
