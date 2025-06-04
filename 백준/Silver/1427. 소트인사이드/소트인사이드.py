import sys
input = sys.stdin.readline

N = int(input().strip())
digits = list(map(int,str(N)))
digits.sort(reverse=True)
result = int(''.join(map(str, digits)))
print(result)