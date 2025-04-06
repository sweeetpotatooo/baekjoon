# 문제
# X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.

# 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

# 입력
# 입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.

# 출력
# 출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.\


import sys
input = sys.stdin.readline

# 제출자 명단을 저장할 리스트
submitted = []
# 28명의 출석번호를 입력받아 리스트에 저장
for _ in range(28):
    submitted.append(int(input().strip()))
# 제출하지 않은 학생의 출석번호를 저장할 리스트
not_submitted = []
# 1부터 30까지의 출석번호 중 제출하지 않은 학생의 번호를 찾는다.
for i in range(1, 31):
    if i not in submitted:
        not_submitted.append(i)
# 제출하지 않은 학생의 출석번호를 오름차순으로 정렬
not_submitted.sort()
# 제출하지 않은 학생의 출석번호를 출력
print(not_submitted[0])
print(not_submitted[1])