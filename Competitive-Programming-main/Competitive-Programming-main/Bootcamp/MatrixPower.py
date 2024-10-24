def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j]+=A[i][k]*B[k][j]

    return result

def matrix_power(A,k):
    if k==0:
        return [[1,0],[0,1]]
    
    if k==1:
        return A
    
    temp=matrix_power(A,k//2)

    if (k&1)==0:
        return matrix_multiply(temp,temp)
    
    else:
        return matrix_multiply(matrix_multiply(temp,temp),A)

A=[[1,2],[3,4]]

result = matrix_power(A,3)

if result:
    print(result)