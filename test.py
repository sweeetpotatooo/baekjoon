import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
num_list = list(map(int, input().split()))

a.sort()

for num in num_list:
    start, end = 0, n - 1
    is_exist = False

    while start <= end:
        mid = (start + end) // 2
        if num == a[mid]:
            is_exist = True
            print(1)
            break
        elif num > a[mid]:
            start = mid + 1
        else:
            end = mid - 1

    if not is_exist:
        print(0)
