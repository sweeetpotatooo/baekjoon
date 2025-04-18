# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.



# import sys
# input = sys.stdin.readline

# n=int(input())
# arr_A = list(map(int, input().split()))
# max_num = 0
# count = 0

# for i in range (n):
#   if max_num < arr_A[i]:
#     max_num=arr_A[i]
#     count+=1
# print(count)


#수정 필요, 현재 코드는 그냥 수열에서 증가하는 길이만 구하는건데 부분수열이라 다르게 접근해야하나?


n = int(input())
A = list(map(int, input().split()))

dp = [1] * n
# dp[i] => i번째 원소를 마지막으로 하는 가장 긴 증가 부분 수열의 길이
# 초기값을 1로 설정 => 모든 수열은 길이 최소 1

for i in range(n):
    #첫 번째 원소부터 차례로 탐색, "현재 위치(i)"를 마지막으로 하는 LIS 길이를 계산
    for j in range(i):
        #0부터 i-1까지 돌면서 "이전의 원소들(j)"과 현재 위치(i)의 원소를 비교합니다.
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            
            #만약 이전 원소 (arr_A[j])가 현재 원소 (arr_A[i])보다 작다면,
            #이전 원소를 마지막으로 하는 LIS(dp[j]) 뒤에 현재 원소를 붙일 수 있습니다.
            # 이때 dp[j] + 1이 "현재 위치까지의 LIS 길이 후보"가 됩니다.1
            # 이를 기존 값(dp[i])과 비교해 더 긴 길이를 저장합니다.

print(max(dp))
