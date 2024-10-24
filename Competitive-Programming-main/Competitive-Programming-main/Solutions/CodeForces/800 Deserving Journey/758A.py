n=int(input())
l=list(map(int,input().split()))
l.sort()
s=0
for i in l:
    s+=(l[-1]-i)
print(s)