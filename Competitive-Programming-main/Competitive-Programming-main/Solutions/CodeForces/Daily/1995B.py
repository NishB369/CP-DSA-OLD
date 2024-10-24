t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    if n*a<(n//2)*b+(n-(n//2)*2)*a:
        print(n*a)
    else:
        print((n//2)*b+(n-(n//2)*2)*a)