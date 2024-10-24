l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
nl=[]
for i in l1:
    if i in l2:
        nl.append(i)
print(nl)