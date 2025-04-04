import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))

arr.sort()

left = 0
right = n - 1

answer = abs(arr[left] + arr[right])
final = [arr[left], arr[right]]

while left < right:
    current_sum = arr[left] + arr[right]

    if abs(current_sum) < answer:
        answer = abs(current_sum)
        final = [arr[left], arr[right]]
        if answer == 0:
            break
    if current_sum < 0:
        left += 1
    else:
        right -= 1

print(final[0], final[1])
