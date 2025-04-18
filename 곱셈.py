# 문제
# 자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

# 출력
# 첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.


import sys

input = sys.stdin.readline


# A^B%C = A^B1%C * A^B2%C

def dnc_mul(A, B, C):
    if B == 1:
        return A % C

    tmp = dnc_mul(A, B // 2, C) # 분할해서 재귀

    if B % 2 == 1:
        return (tmp * tmp) % C * A % C

    else:
        return (tmp * tmp) % C

A, B, C = map(int, input().split())

print(dnc_mul(A, B, C))
