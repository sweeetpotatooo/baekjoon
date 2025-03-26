
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())  # 앵무새 숫자
parrots = [] # 각 앵무새들이 말한 문장 리스트

for _ in range(N):
    parrots.append(deque(input().split())) # 앵무새가 말한 문장
write_down = deque(input().split()) # 받아 적은 문장

for word in write_down:
    found = False
    for parrot in parrots:
        if parrot and parrot[0] == word:
            parrot.popleft()  # 앵무새 단어를 제거
            found = True
            break
    # 모든 앵무새: 현재 단어를 말할 수 없음
    if not found:
        print("Impossible")
        sys.exit(0)

# 모든 앵무새 문장이 완전히 소진 확인.
if all(not parrot for parrot in parrots):
    print("Possible")
else:
    print("Impossible")
