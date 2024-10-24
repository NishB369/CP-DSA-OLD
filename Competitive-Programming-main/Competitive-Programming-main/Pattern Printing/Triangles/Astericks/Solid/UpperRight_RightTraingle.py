n=int(input())
s=0
for i in range(n,0,-1):
    print(' '*s,end='')
    print('*'*i)
    s+=1