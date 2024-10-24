nl=[]
for i in range(5):
    l=input().split()
    nl.append(l)
for i in range(len(nl)):
    for j in range(len(nl[i])):
        if nl[i][j]=='1':
            a=i
            b=j
        
if (2-a)<0:
    a=4-a
    
if (2-b)<0:
    b=4-b
    
print((2-a)+(2-b))