import sys                        
input = sys.stdin.readline        
N, S = map(int, input().split())  
arr = list(map(int, input().split()))
count = 0                        


for bit in range(1, 1<<N):
    sum = 0
    for i in range(N):
        if bit & (1<<i):
            sum += arr[i]
    if sum == S:
        count += 1
print(count)