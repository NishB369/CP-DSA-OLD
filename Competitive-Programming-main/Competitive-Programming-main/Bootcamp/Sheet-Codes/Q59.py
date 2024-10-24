l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
nl=l1
for i in l2:
    if i not in nl:
        nl.append(i)
print(nl)