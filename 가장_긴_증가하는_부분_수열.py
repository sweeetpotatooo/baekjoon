# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.



import sys
input = sys.stdin.readline

n=int(input())
arr_A = list(map(int, input().split()))
max_num = 0
count = 0

for i in range (n):
  if max_num < arr_A[i]:
    max_num=arr_A[i]
    count+=1
print(count)


#수정 필요, 현재 코드는 그냥 수열에서 증가하는 길이만 구하는건데 부분수열이라 다르게 접근해야하나?
