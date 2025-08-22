import sys
input = sys.stdin.readline
def triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"
    elif a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    print(triangle_type(a, b, c))
    