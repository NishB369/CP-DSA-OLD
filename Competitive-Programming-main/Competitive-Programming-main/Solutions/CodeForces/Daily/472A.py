n=int(input())
def func(m):
    for i in range(2,int(m**0.5)+1):
        if m%i==0:
            return True
    return False

for i in range(4,n//2+1):
    if func(i) and func(n-i):
        print(i,n-i)
        break