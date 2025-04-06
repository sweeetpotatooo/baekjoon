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