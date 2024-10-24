t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(len(l)):
        if l.count(l[i])==1:
            print(i+1)
            break