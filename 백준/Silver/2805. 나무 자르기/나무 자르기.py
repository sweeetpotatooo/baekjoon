import sys
input = sys.stdin.readline


n, m = map(int,input().split())
tree_height = list(map(int,input().split()))
tree_height.sort()

start, end = 0, max(tree_height)

while start<= end:
  mid = (start+end) // 2
  total = 0

  for i in tree_height:
    if i >= mid:
      total += i - mid

  if total >= m:
      start = mid + 1
  else:
      end = mid - 1
print(end)