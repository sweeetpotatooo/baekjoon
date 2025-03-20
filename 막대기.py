#아래 그림처럼 높이만 다르고 (같은 높이의 막대기가 있을 수 있음) 모양이 같은 막대기를 일렬로 세운 후, 왼쪽부터 차례로 번호를 붙인다. 
# 각 막대기의 높이는 그림에서 보인 것처럼 순서대로 6, 9, 7, 6, 4, 6 이다. 일렬로 세워진 막대기를 오른쪽에서 보면 보이는 막대기가 있고 보이지 않는 막대기가 있다. 
# 즉, 지금 보이는 막대기보다 뒤에 있고 높이가 높은 것이 보이게 된다. 예를 들어, 그림과 같은 경우엔 3개(6번, 3번, 2번)의 막대기가 보인다.

import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    stack.append(int(input()))

count = 0
max_height = 0 

for i in range(n-1, -1, -1):
    if stack[i] > max_height:  
        count += 1
        max_height = stack[i]  

print(count)
