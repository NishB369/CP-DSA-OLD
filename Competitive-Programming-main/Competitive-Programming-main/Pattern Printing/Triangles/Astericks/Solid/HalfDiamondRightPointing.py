m=int(input())
n=m//2
if m&1==0:
    for i in range(1,n+1):
        print(i*'*')
    for i in range(n,0,-1):
        print('*'*i)
else:
    n=n+1
    for i in range(1,n+1):
        print(i*'*')
    for i in range(n-1,0,-1):
        print('*'*i)