t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    a=l[0]
    l.sort()
    b=l.index(a)
    print(len(l)-b-1)