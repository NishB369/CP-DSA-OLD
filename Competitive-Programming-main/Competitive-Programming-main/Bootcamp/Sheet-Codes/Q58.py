def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        print("Cannot multiply the matrices. Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
        return None

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j]+=A[i][k]*B[k][j]

    return result

A=eval(input('Enter matrix A as nested list: '))
B=eval(input('Enter matrix B as nested list: '))

result = matrix_multiply(A, B)


if result:
    print("Result of matrix multiplication (A * B):")
    # for row in result:
    #     print(row)
    print(result)