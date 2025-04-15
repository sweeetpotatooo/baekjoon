import sys
input = sys.stdin.readline

# 5개의 단어를 각각 문자열로 저장합니다.
matrix = []
for _ in range(5):
    row = input().rstrip()  # 오른쪽 공백 제거 (개행문자 제거)
    matrix.append(row)

# 가장 긴 단어의 길이를 구합니다.
max_length = max(len(row) for row in matrix)

result = ""
for i in range(max_length):
    for word in matrix:
        if i < len(word):
            result += word[i]

print(result)
