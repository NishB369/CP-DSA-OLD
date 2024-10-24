l=list(map(int,input('Enter a list of space seprated integers: ').split()))
k=int(input())
print(l[k:]+l[:k])