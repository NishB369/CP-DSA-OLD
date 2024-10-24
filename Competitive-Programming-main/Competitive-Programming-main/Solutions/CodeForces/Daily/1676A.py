t=int(input())
for i in range(t):
    n=int(input())
    
    if len(str(n))<6:
        a=str(0)*(6-len(str(n)))+str(n)
    else:
        a=str(n)
        
    s1=0
    for i in a[:3]:
        s1+=int(i)
    s2=0
    for i in a[3:]:
        s2+=int(i)
        
    print("YES") if s1==s2 else print('NO')
