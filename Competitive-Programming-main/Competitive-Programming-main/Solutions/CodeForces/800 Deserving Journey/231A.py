n = int(input())
c=0
for i in range(n):
    l=map(int,input().split())
    if sum(l)>=2:
        c+=1
print(c)