m=int(input('Enter number of rows: '))
n=m//2
s=(2*n-1)//2
for i in range(1,2*n,2):
    print(' '*s,end='')
    print('*'*i)
    s-=1
s=0
for i in range(2*n-1,0,-2):
    print(' '*s,end='')
    print('*'*i)
    s+=1