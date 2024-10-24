n=int(input())
s=0
for i in range(n):
    a,b=map(int,input().split())
    if (b-a)>=2:
        s+=1
print(s)