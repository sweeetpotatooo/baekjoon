
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