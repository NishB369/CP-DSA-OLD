def matrix_square(A):
    rows_A = len(A)
    cols_A = len(A[0])

    result = [[0 for _ in range(cols_A)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_A):
            for k in range(cols_A):
                result[i][j]+=A[i][k]*A[k][j]

    return result

A=eval(input('Enter square matrix A as nested list: '))

result = matrix_square(A)

if result:
    print(result)