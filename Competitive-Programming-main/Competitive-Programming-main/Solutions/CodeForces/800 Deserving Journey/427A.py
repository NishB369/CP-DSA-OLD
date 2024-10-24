n = int(input())
l=list(map(int,input().split()))
t=0
ans=0
for p in l:
    if p==-1:
        if t==0:
            ans+=1
        else:
            t-=1
    else:
        t+=p
print(ans)