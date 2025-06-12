import sys
input = sys.stdin.readline
 
N = int(input())
my_list = sorted(map(int, input().split()))
M = int(input())
card_list = map(int, input().split())
 
dic = {}
for i in my_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
 
def binarySearch(target, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    
    if target == my_list[mid]:
        return dic[target]
    elif target > my_list[mid]:
        return binarySearch(target, mid + 1, end)
    elif target < my_list[mid]:
        return binarySearch(target, start, mid - 1)
 
for target in card_list:
    print(binarySearch(target, 0, N - 1), end=" ")
