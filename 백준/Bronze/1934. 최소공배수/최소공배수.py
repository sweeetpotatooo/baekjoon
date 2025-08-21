import sys
input = sys.stdin.readline
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B))
    