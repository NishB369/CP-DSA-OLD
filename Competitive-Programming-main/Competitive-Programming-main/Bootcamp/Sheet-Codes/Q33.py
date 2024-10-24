n=int(input('Enter the first term of GP: '))
r=int(input('Enter the common ration for GP: '))
l=int(input('Enter the limit for GP: '))

for i in range(1,l+1):
    print(n,end=' ')
    n*=r