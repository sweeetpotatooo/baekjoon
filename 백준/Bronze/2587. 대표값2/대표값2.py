import sys
input = sys.stdin.readline
data = []
for _ in range(5):
    data.append(int(input()))
data.sort()
print(sum(data)//5)
print(data[2])