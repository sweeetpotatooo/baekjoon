import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
else:
    opinions = [int(input().strip()) for _ in range(n)]
    opinions.sort()
    
    k = int(n * 0.15 + 0.5)
    trimmed_opinions = opinions[k:n-k] if k > 0 else opinions
    average = int(sum(trimmed_opinions) / len(trimmed_opinions) + 0.5)
    print(average)
