
import sys
input = sys.stdin.readline

n = int(input())
stack = []
count = 1
result = []  # '+'와 '-'를 임시로 저장할 리스트
possible = True  # 수열을 만들 수 있는지 여부

for _ in range(n):
    num = int(input())

    # num에 도달할 때까지 push
    while count <= num:
        stack.append(count)
        result.append('+')
        count += 1

    # 스택의 top이 num이면 pop
    if stack and stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        # 만들 수 없는 경우
        possible = False
        break

if possible:
    # 만들 수 있다면, 지금까지 저장한 '+'와 '-' 출력
    print('\n'.join(result))
else:
    # 만들 수 없다면, 오직 NO만 출력
    print('NO')
