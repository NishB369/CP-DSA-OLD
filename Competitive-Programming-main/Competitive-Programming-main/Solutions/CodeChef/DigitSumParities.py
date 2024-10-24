def func(m):
    s=0
    for i in str(m):
        s+=int(i)
    return s

t=int(input())
for _ in range(t):
    n=int(input())
    if func(n)%2!=func(n+1)%2:
        print(n+1)
    else:
        print(n+2)