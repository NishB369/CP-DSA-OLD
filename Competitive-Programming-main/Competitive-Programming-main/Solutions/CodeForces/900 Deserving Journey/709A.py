n,b,d=map(int,input().split())
l=list(map(int,input().split()))
s=0
c=0
for i in l:
    if i>b:
        continue
    else:
        s+=i
        if s>d:
            c+=1
            s=0
print(c)