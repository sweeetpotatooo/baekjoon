import sys
from collections import Counter
input = sys.stdin.readline
n = int(input().strip())
numbers = [int(input().strip()) for _ in range(n)]
# 산술평균
mean = round(sum(numbers) / n)
# 중앙값
numbers.sort()
median = numbers[n // 2]
# 최빈값
frequency = Counter(numbers)
most_common = frequency.most_common()
if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
    mode = sorted([x[0] for x in most_common if x[1] == most_common[0][1]])[1]
else:
    mode = most_common[0][0]
# 범위
range_value = max(numbers) - min(numbers)
print(mean)
print(median)
print(mode)
print(range_value)