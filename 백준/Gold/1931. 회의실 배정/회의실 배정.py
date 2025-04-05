import sys
input = sys.stdin.readline

n = int(input())

time = []
for _ in range(n):
  start, end = map(int,input().strip().split())
  time.append([start, end])
time.sort(key=lambda x : (x[1],x[0]))

count = 1
end = time[0][1]
for i in range(1, n):
    if time[i][0]>=end:
        end = time[i][1]
        count += 1

print(count)