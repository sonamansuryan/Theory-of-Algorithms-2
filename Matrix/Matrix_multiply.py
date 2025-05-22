def matrix_multiply(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    C11 = matrix_add(matrix_multiply(A11, B11), matrix_multiply(A12, B21))
    C12 = matrix_add(matrix_multiply(A11, B12), matrix_multiply(A12, B22))
    C21 = matrix_add(matrix_multiply(A21, B11), matrix_multiply(A22, B21))
    C22 = matrix_add(matrix_multiply(A21, B12), matrix_multiply(A22, B22))

    C = [[0] * n for i in range(n)]
    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]

    return C


def matrix_add(X, Y):
    n = len(X)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = X[i][j] + Y[i][j]
    return result


A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
B = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

C = matrix_multiply(A, B)
print("Result matrix:")
for row in C:
    print(row)