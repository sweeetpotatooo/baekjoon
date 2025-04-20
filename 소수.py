# 문제
# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

# 입력
# 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

# M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

# 출력
# M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 

# 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

import sys
input = sys.stdin.readline

M = int(input())
N = int(input())
demical = []

for num in range(M, N+1): # M이상 ~ N이하의 수
    count = 0 # 나눠지는 수가 있으면 카운트
    if num > 1: # 2이상의 수들 중에 소수를 찾는다.
        for i in range(2, num): # 2~num에서 나눠지는 수를 찾는다
            if num % i == 0: # 나머지가 0이면 나눠지는 수(소수 아님)
                count += 1 # 소수가 아님을 카운트
                break
        if count == 0: # 나눠지는 수가 없으면 소수
            demical.append(num)


if len(demical) > 0:
    print(sum(demical))
    print(min(demical))
else:
    print(-1)