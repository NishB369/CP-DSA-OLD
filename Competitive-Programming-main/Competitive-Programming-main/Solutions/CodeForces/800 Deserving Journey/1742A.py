t=int(input())
for i in range(t):
    flag=False
    a,b,c=map(int,input().split())
    l=[a,b,c]
    for i in l:
        if i==sum(l)-i:
            flag=True
            break
    if flag==True:
        print("YES")
    else:
        print("NO")
        