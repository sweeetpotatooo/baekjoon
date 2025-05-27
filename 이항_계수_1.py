# 이항 계수를 구하는 프로그램을 작성하시오.

import sys
import math
input = sys.stdin.readline

N, K = map(int, input().split())

result = math.factorial(N)/(math.factorial(K)*math.factorial(N-K))
print(int(result))
