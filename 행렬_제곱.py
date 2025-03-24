# 문제
# 크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 
# 수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

# 입력
# 첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)
# 둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

# 출력
# 첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.

N,B = map(int,input().split())
matrix = []
for i in range(N):
  row = list(map(int,input().split()))
  matrix.append(row)

# 행렬 곱
def multiply_matrix(A, B):
    result = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(0)
        result.append(row)

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % 1000
    return result

# 행렬 제곱
def matrix_square(matrix, exponent):
    if exponent == 1:
        return [[element % 1000 for element in row] for row in matrix]
    #지수 짝수
    if exponent % 2 == 0:
        half = matrix_square(matrix, exponent // 2)
        return multiply_matrix(half, half)
    # 지수 홀수
    else:
        return multiply_matrix(matrix_square(matrix, exponent - 1), matrix)

result = matrix_square(matrix, B)

for row in result:
    print(' '.join(map(str, row)))