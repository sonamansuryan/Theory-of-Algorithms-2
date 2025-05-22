def multiply_matrix(A, B):
    n = len(A)
    result = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]

    print("Մատրիցի արդյունք: ")
    for row in result:
        print(row)
    return result


n = int(input("Մուտքագրեք մատրիցի չափը: "))
print("Մուտքագրեք առաջին մատրիցը: ")
A = [list(map(int, input().split())) for i in range(n)]
print("Մուտքագրեք երկրորդ մատրիցը թվերը բացատներով բաժանելով: ")
B = [list(map(int, input().split())) for i in range(n)]

M = multiply_matrix(A, B)
