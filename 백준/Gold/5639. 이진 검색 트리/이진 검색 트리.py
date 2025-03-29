import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

pre = []
while True:
    try:
        x = int(input())
        pre.append(x)
    except:
        break

def post(start, end):
    if start >= end:
        return
    root = pre[start]
    mid = start + 1
    while mid < end and pre[mid] < root:
        mid += 1
    post(start+1, mid)
    post(mid, end)
    print(root)

post(0, len(pre))

