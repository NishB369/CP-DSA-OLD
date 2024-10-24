n=int(input('Enter number of rows: '))
s=0
for i in range(2*n-1,0,-2):
    print(' '*s,end='')
    print('*'*i)
    s+=1