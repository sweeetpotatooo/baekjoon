import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

max_val = -10**9
min_val = 10**9

def dfs(idx, current, add, sub, mul, div):
    global max_val, min_val
    if idx == n:
        max_val = max(max_val, current)
        min_val = min(min_val, current)
        return
    if add > 0:
        dfs(idx+1, current + nums[idx], add-1, sub, mul, div)
    if sub > 0:
        dfs(idx+1, current - nums[idx], add, sub-1, mul, div)
    if mul > 0:
        dfs(idx+1, current * nums[idx], add, sub, mul-1, div)

    if div > 0:
        if current < 0:
            dfs(idx+1, - (abs(current) // nums[idx]), add, sub, mul, div-1)
        else:
            dfs(idx+1, current // nums[idx], add, sub, mul, div-1)

dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3])
print(max_val)
print(min_val)
