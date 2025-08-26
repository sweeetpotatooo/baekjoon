import sys
input = sys.stdin.readline
x, y = map(int, input().split())
days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
month = [31, 28, 31,  30, 31, 30, 31, 31, 30, 31, 30, 31]
total = 0
for i in range(x-1):
    total += month[i]
total += y
print(days[total % 7])