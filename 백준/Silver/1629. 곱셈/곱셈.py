
import sys

input = sys.stdin.readline


def dnc_mul(A, B, C):
    if B == 1:
        return A % C

    tmp = dnc_mul(A, B // 2, C)

    if B % 2 == 1:
        return (tmp * tmp) % C * A % C

    else:
        return (tmp * tmp) % C

A, B, C = map(int, input().split())

print(dnc_mul(A, B, C))
