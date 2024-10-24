m=int(input())
n=m//2
s=n-1
if m&1==0:
    for i in range(1,n+1):
        print(' '*s,end='')
        print(i*'*')
        s-=1
    s=0
    for i in range(n,0,-1):
        print(' '*s,end='')
        print('*'*i)
        s+=1
else:
    n=n+1
    s=n-1
    for i in range(1,n+1):
        print(' '*s,end='')
        print(i*'*')
        s-=1
    s=1
    for i in range(n-1,0,-1):
        print(' '*s,end='')
        print('*'*i)
        s+=1