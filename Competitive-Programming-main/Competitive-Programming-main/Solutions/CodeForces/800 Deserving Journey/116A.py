n=int(input())
s=0
l=[]
for i in range(n):
    c=0
    a,b=map(int,input().split())
    c+=b-a
    s+=c
    l.append(s)
print(max(l))