import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
nums = list(map(int, input().split()))

def binary_search(target):
    left = 0
    right = len(cards) - 1
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == target:
            return 1
        elif cards[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

result = []
for num in nums:
    result.append(str(binary_search(num)))

print(" ".join(result))