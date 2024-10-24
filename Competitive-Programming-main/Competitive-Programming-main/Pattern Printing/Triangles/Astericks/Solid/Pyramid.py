n=int(input('Enter number of rows: '))
s=(2*n-1)//2
for i in range(1,2*n,2):
    print(' '*s,end='')
    print('*'*i)
    s-=1