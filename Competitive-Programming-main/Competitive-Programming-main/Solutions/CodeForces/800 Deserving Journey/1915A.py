t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    l=[a,b,c]
    for i in l:
        if l.count(i)==1:
            print(i)
            break