import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(set(arr))
compression = {value: index for index, value in enumerate(sorted_arr)}
result = [compression[x] for x in arr]
print(' '.join(map(str, result)))