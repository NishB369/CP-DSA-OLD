a,k,n=map(int,input().split())
sum=round(n/2*(2*a+(n-1)*a))
if sum>k:
    print(sum-k)
else:
    print(0)